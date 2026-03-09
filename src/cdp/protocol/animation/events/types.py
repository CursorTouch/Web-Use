"""CDP Animation Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.animation.types import Animation

class animationCanceledEvent(TypedDict, total=True):
    id: str
    """Id of the animation that was cancelled."""
class animationCreatedEvent(TypedDict, total=True):
    id: str
    """Id of the animation that was created."""
class animationStartedEvent(TypedDict, total=True):
    animation: Animation
    """Animation that was started."""
class animationUpdatedEvent(TypedDict, total=True):
    animation: Animation
    """Animation that was updated."""