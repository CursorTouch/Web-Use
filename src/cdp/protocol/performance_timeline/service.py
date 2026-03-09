"""CDP PerformanceTimeline Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import PerformanceTimelineMethods
from .events.service import PerformanceTimelineEvents

if TYPE_CHECKING:
    from ...service import Client

class PerformanceTimeline(PerformanceTimelineMethods, PerformanceTimelineEvents):
    """
    Reporting of performance timeline events, as specified in https://w3c.github.io/performance-timeline/#dom-performanceobserver.
    """
    def __init__(self, client: Client):
        """
        Initialize the PerformanceTimeline domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        PerformanceTimelineMethods.__init__(self, client)
        PerformanceTimelineEvents.__init__(self, client)