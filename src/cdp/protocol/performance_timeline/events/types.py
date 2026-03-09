"""CDP PerformanceTimeline Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.performance_timeline.types import TimelineEvent

class timelineEventAddedEvent(TypedDict, total=True):
    event: TimelineEvent