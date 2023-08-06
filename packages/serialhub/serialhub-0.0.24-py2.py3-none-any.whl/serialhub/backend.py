#!/usr/bin/env python
# coding: utf-8

# Copyright (c) cdr4eelz.
# Distributed under the terms of the Modified BSD License.

"""
SerialHub backend widget & support classes
"""

#from __future__ import print_function
from typing import Sequence, Mapping, Any, ByteString, Optional, NoReturn #, BinaryIO, IO
import io #, binascii

from ipywidgets import DOMWidget, register
import traitlets #from traitlets import Unicode, Int, Bool, Complex, Enum
from ._frontend import module_name, module_version

@register
class SerialHubWidget(DOMWidget):
    """
    SerialHubWidget class inherits ipywidgets.DOMWidget
      Model: SerialHubModel, View: SerialHubView
      Synchronized attributes: value (Unicode), status (Unicode)
    """
    _model_name = traitlets.Unicode('SerialHubModel').tag(sync=True)
    _model_module = traitlets.Unicode(module_name).tag(sync=True)
    _model_module_version = traitlets.Unicode(module_version).tag(sync=True)
    _view_name = traitlets.Unicode('SerialHubView').tag(sync=True)
    _view_module = traitlets.Unicode(module_name).tag(sync=True)
    _view_module_version = traitlets.Unicode(module_version).tag(sync=True)

    isSupported = traitlets.Bool(allow_none=True, read_only=True).tag(sync=True)
    #TODO: Use an Enum() rather than string
    status = traitlets.Unicode(default_value='Checking...').tag(sync=True)
    value = traitlets.Unicode(default_value='').tag(sync=True)
    pkt_recv_front = traitlets.Int(default_value=0, read_only=True).tag(sync=True)
    pkt_recv_back = traitlets.Int(default_value=0).tag(sync=True)
    pkt_send_front = traitlets.Int(default_value=0, read_only=True).tag(sync=True)
    pkt_send_back = traitlets.Int(default_value=0).tag(sync=True)

    def __init__(self, *args, **kwargs):
        DOMWidget.__init__(self, *args, **kwargs)
        self.on_msg(self.msg_custom)

    def msg_custom(self,
                widget: DOMWidget,  # Same as self, in this case, a SerialHubWidget
                content: Mapping[str, Any],
                buffers: Optional[Sequence[ByteString]] = None
    ) -> None:
        """
        msg_custom() method receives custom message callbacks from the frontend client
        """
        msgtype = str(content['type'])
        if msgtype == 'RECV':
            self.pkt_recv_back += 1
            for buf in buffers:
                #decoded: str = buf.hex()
                #decoded: str = str(binascii.b2a_hex(buf))
                #decoded: str = buf.decode('ascii','ignore')
                decoded: str = str(buf, encoding='ascii', errors='ignore')
                self.value += decoded.replace("\n", "\\n").replace("\r", "\\r")
        elif msgtype == 'text': #Leftover test message
            self.value += content['text']

    def send_custom(self,
                content: Mapping[str, Any],
                buffers: Optional[Sequence[ByteString]] = None
    ) -> None:
        """
        send_custom(self,content,buffers) sends custom message to frontend
        """
        self.send(content, buffers)

    def write_bytes(self,
                data: ByteString
    ) -> None:
        """
        write_bytes() sends a single buffer for the client to write() as serial data
        """
        self.send_custom({'type': 'SEND'}, [data])
        self.pkt_send_back += 1

    def write_str(self,
                data: str,
                enc: Optional[str] = 'ascii',
                errs: Optional[str] = 'ignore'
    ) -> None:
        """
        write_str() sends a single buffer for the client to write() as serial data
        """
        self.send_custom(
            {'type': 'SEND'},
            [data.encode(encoding=enc, errors=errs)]
        )
        self.pkt_send_back += 1


#BinaryIO(IO[bytes])
class Serial(io.RawIOBase):
    """
    Serial IO proxied to frontend browser serial
    """
    def __init__(self, *args, **kwargs):
        io.RawIOBase.__init__(self)

    def readable(self) -> bool:
        return True
    def writable(self) -> bool:
        return True
    def isatty(self)   -> bool:
        return False
    def seekable(self) -> bool:
        return False

    def closed(self) -> bool:
        return True

    def write(self, data: bytes) -> Optional[int]:
        if self.closed():
            raise ValueError("Stream closed")
        return 0

    def readinto(self, b: bytearray) -> Optional[int]:
        if self.closed():
            raise ValueError("Stream closed")
        if len(b) <= 0:
            return None
        b[0] = 0
        return 1

    def fileno(self) -> NoReturn:
        raise OSError('No fileno')
    def tell(self) -> NoReturn:
        raise OSError('Not seekable')
    def seek(self, offset: int, whence = 0) -> NoReturn:
        raise OSError('Not seekable')
    def truncate(self, size: Optional[int] = None) -> NoReturn:
        raise OSError('Not seekable')
