"""CDP PerformanceTimeline Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PerformanceTimelineEvents:
    """
    Events for the PerformanceTimeline domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the PerformanceTimeline events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_timeline_event_added(self, callback: Callable[[timelineEventAddedEvent, str | None], None] | None = None) -> None:
        """
    Sent when a performance timeline event is added. See reportPerformanceTimeline method.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: timelineEventAddedEvent, session_id: str | None).
        """
        self.client.on('PerformanceTimeline.timelineEventAdded', callback)