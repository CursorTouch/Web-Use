"""CDP SmartCardEmulation Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.smart_card_emulation.types import ConnectionState
    from cdp.protocol.smart_card_emulation.types import Protocol
    from cdp.protocol.smart_card_emulation.types import ReaderStateOut
    from cdp.protocol.smart_card_emulation.types import ResultCode



class reportEstablishContextResultParameters(TypedDict, total=True):
    requestId: str
    contextId: int
class reportReleaseContextResultParameters(TypedDict, total=True):
    requestId: str
class reportListReadersResultParameters(TypedDict, total=True):
    requestId: str
    readers: List[str]
class reportGetStatusChangeResultParameters(TypedDict, total=True):
    requestId: str
    readerStates: List[ReaderStateOut]
class reportBeginTransactionResultParameters(TypedDict, total=True):
    requestId: str
    handle: int
class reportPlainResultParameters(TypedDict, total=True):
    requestId: str
class reportConnectResultParameters(TypedDict, total=True):
    requestId: str
    handle: int
    activeProtocol: NotRequired[Protocol]
class reportDataResultParameters(TypedDict, total=True):
    requestId: str
    data: str
class reportStatusResultParameters(TypedDict, total=True):
    requestId: str
    readerName: str
    state: ConnectionState
    atr: str
    protocol: NotRequired[Protocol]
class reportErrorParameters(TypedDict, total=True):
    requestId: str
    resultCode: ResultCode