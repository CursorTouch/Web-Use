"""CDP Emulation Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.emulation.types import ScreenOrientation

class virtualTimeBudgetExpiredEvent(TypedDict, total=True):
    pass
class screenOrientationLockChangedEvent(TypedDict, total=True):
    locked: bool
    """Whether the screen orientation is currently locked."""
    orientation: NotRequired[ScreenOrientation]
    """The orientation lock type requested by the page. Only set when locked is true."""