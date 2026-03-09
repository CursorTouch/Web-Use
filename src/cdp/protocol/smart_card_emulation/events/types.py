"""CDP SmartCardEmulation Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.smart_card_emulation.types import Disposition
    from cdp.protocol.smart_card_emulation.types import Protocol
    from cdp.protocol.smart_card_emulation.types import ProtocolSet
    from cdp.protocol.smart_card_emulation.types import ReaderStateIn
    from cdp.protocol.smart_card_emulation.types import ShareMode

class establishContextRequestedEvent(TypedDict, total=True):
    requestId: str
class releaseContextRequestedEvent(TypedDict, total=True):
    requestId: str
    contextId: int
class listReadersRequestedEvent(TypedDict, total=True):
    requestId: str
    contextId: int
class getStatusChangeRequestedEvent(TypedDict, total=True):
    requestId: str
    contextId: int
    readerStates: List[ReaderStateIn]
    timeout: NotRequired[int]
    """in milliseconds, if absent, it means "infinite""""
class cancelRequestedEvent(TypedDict, total=True):
    requestId: str
    contextId: int
class connectRequestedEvent(TypedDict, total=True):
    requestId: str
    contextId: int
    reader: str
    shareMode: ShareMode
    preferredProtocols: ProtocolSet
class disconnectRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
    disposition: Disposition
class transmitRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
    data: str
    protocol: NotRequired[Protocol]
class controlRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
    controlCode: int
    data: str
class getAttribRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
    attribId: int
class setAttribRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
    attribId: int
    data: str
class statusRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
class beginTransactionRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
class endTransactionRequestedEvent(TypedDict, total=True):
    requestId: str
    handle: int
    disposition: Disposition