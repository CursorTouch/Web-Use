"""CDP Log Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.log.types import LogEntry

class entryAddedEvent(TypedDict, total=True):
    entry: LogEntry
    """The entry."""