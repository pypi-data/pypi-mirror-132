"""IPython kernel for parallel computing"""
import sys

from ipykernel.ipkernel import IPythonKernel
from traitlets import Integer
from traitlets import Type

from .datapub import ZMQDataPublisher
from ipyparallel.serialize import serialize_object
from ipyparallel.serialize import unpack_apply_message
from ipyparallel.util import utcnow


class IPythonParallelKernel(IPythonKernel):
    """Extend IPython kernel for parallel computing"""

    engine_id = Integer(-1)
    msg_types = getattr(IPythonKernel, 'msg_types', []) + ['apply_request']
    control_msg_types = getattr(IPythonKernel, 'control_msg_types', []) + [
        'abort_request',
        'clear_request',
    ]
    _execute_sleep = 0
    data_pub_class = Type(ZMQDataPublisher)

    def _topic(self, topic):
        """prefixed topic for IOPub messages"""
        base = "engine.%s" % self.engine_id

        return f"{base}.{topic}".encode()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # add apply_request, in anticipation of upstream deprecation
        self.shell_handlers['apply_request'] = self.apply_request
        # set up data pub
        data_pub = self.shell.data_pub = self.data_pub_class(parent=self)
        self.shell.configurables.append(data_pub)
        data_pub.session = self.session
        data_pub.pub_socket = self.iopub_socket
        self.aborted = set()

    def should_handle(self, stream, msg, idents):
        """Check whether a shell-channel message should be handled

        Allows subclasses to prevent handling of certain messages (e.g. aborted requests).
        """
        if not super().should_handle(stream, msg, idents):
            return False
        msg_id = msg['header']['msg_id']
        msg_type = msg['header']['msg_type']
        if msg_id in self.aborted:
            # is it safe to assume a msg_id will not be resubmitted?
            self.aborted.remove(msg_id)
            self._send_abort_reply(stream, msg, idents)
            return False
        self.log.info(f"Handling {msg_type}: {msg_id}")
        return True

    def init_metadata(self, parent):
        """init metadata dict, for execute/apply_reply"""
        parent_metadata = parent.get('metadata', {})
        return {
            'started': utcnow(),
            'dependencies_met': True,
            'engine': self.ident,
            'is_broadcast': parent_metadata.get('is_broadcast', False),
            'is_coalescing': parent_metadata.get('is_coalescing', False),
            'original_msg_id': parent_metadata.get('original_msg_id', ''),
        }

    def finish_metadata(self, parent, metadata, reply_content):
        """Finish populating metadata.

        Run after completing a request handler.
        """
        metadata['status'] = reply_content['status']
        if reply_content['status'] == 'error':
            if reply_content['ename'] == 'UnmetDependency':
                metadata['dependencies_met'] = False
            metadata['engine_info'] = dict(
                engine_uuid=self.ident,
                engine_id=self.engine_id,
            )

        return metadata

    def apply_request(self, stream, ident, parent):
        try:
            content = parent['content']
            bufs = parent['buffers']
            msg_id = parent['header']['msg_id']
        except:
            self.log.error("Got bad msg: %s", parent, exc_info=True)
            return

        md = self.init_metadata(parent)
        reply_content, result_buf = self.do_apply(content, bufs, msg_id, md)

        # put 'ok'/'error' status in header, for scheduler introspection:
        md = self.finish_metadata(parent, md, reply_content)

        # flush i/o
        sys.stdout.flush()
        sys.stderr.flush()
        self.log.debug(f'Sending apply_reply: {msg_id}')
        self.session.send(
            stream,
            'apply_reply',
            reply_content,
            parent=parent,
            ident=ident,
            buffers=result_buf,
            metadata=md,
        )

    def do_apply(self, content, bufs, msg_id, reply_metadata):
        shell = self.shell
        try:
            working = shell.user_ns

            prefix = "_" + str(msg_id).replace("-", "") + "_"

            f, args, kwargs = unpack_apply_message(bufs, working, copy=False)

            fname = getattr(f, '__name__', 'f')

            fname = prefix + "f"
            argname = prefix + "args"
            kwargname = prefix + "kwargs"
            resultname = prefix + "result"

            ns = {fname: f, argname: args, kwargname: kwargs, resultname: None}
            # print ns
            working.update(ns)
            code = f"{resultname} = {fname}(*{argname},**{kwargname})"
            try:
                exec(code, shell.user_global_ns, shell.user_ns)
                result = working.get(resultname)
            finally:
                for key in ns:
                    working.pop(key)

            result_buf = serialize_object(
                result,
                buffer_threshold=self.session.buffer_threshold,
                item_threshold=self.session.item_threshold,
            )

        except BaseException as e:
            # invoke IPython traceback formatting
            # this sends the 'error' message
            shell.showtraceback()

            try:
                str_evalue = str(e)
            except Exception as str_error:
                str_evalue = f"Failed to cast exception to string: {str_error}"
            reply_content = {
                'traceback': [],
                'ename': str(type(e).__name__),
                'evalue': str_evalue,
            }
            # get formatted traceback, which ipykernel recorded
            if hasattr(shell, '_last_traceback'):
                # ipykernel 4.4
                reply_content['traceback'] = shell._last_traceback or []
            else:
                self.log.warning("Didn't find a traceback where I expected to")
            shell._last_traceback = None
            e_info = dict(engine_uuid=self.ident, engine_id=self.int_id, method='apply')
            reply_content['engine_info'] = e_info

            self.log.info(
                "Exception in apply request:\n%s", '\n'.join(reply_content['traceback'])
            )
            result_buf = []
            reply_content['status'] = 'error'
        else:
            reply_content = {'status': 'ok'}

        return reply_content, result_buf

    # Control messages for msgspec extensions:

    def abort_request(self, stream, ident, parent):
        """abort a specific msg by id"""
        msg_ids = parent['content'].get('msg_ids', None)
        if isinstance(msg_ids, str):
            msg_ids = [msg_ids]
        if not msg_ids:
            self._abort_queues()
        for mid in msg_ids:
            self.aborted.add(str(mid))

        content = dict(status='ok')
        reply_msg = self.session.send(
            stream, 'abort_reply', content=content, parent=parent, ident=ident
        )
        self.log.debug("%s", reply_msg)

    def clear_request(self, stream, idents, parent):
        """Clear our namespace."""
        self.shell.reset(False)
        content = dict(status='ok')
        self.session.send(
            stream, 'clear_reply', ident=idents, parent=parent, content=content
        )

    def _send_abort_reply(self, stream, msg, idents):
        """Send a reply to an aborted request"""
        # FIXME: forward-port ipython/ipykernel#684
        self.log.info(
            f"Aborting {msg['header']['msg_id']}: {msg['header']['msg_type']}"
        )
        reply_type = msg["header"]["msg_type"].rsplit("_", 1)[0] + "_reply"
        status = {"status": "aborted"}
        md = self.init_metadata(msg)
        md = self.finish_metadata(msg, md, status)
        md.update(status)

        self.session.send(
            stream,
            reply_type,
            metadata=md,
            content=status,
            parent=msg,
            ident=idents,
        )
