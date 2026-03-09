"""CDP Cast Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.cast.types import Sink

class sinksUpdatedEvent(TypedDict, total=True):
    sinks: List[Sink]
class issueUpdatedEvent(TypedDict, total=True):
    issueMessage: str