"""CDP Input Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.input.types import DragData

class dragInterceptedEvent(TypedDict, total=True):
    data: DragData