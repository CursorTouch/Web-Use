"""CDP Tracing Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class TracingEvents:
    """
    Events for the Tracing domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Tracing events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_buffer_usage(self, callback: Callable[[bufferUsageEvent, str | None], None] | None = None) -> None:
        """
    No description available for bufferUsage.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: bufferUsageEvent, session_id: str | None).
        """
        self.client.on('Tracing.bufferUsage', callback)
    def on_data_collected(self, callback: Callable[[dataCollectedEvent, str | None], None] | None = None) -> None:
        """
    Contains a bucket of collected trace events. When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by tracingComplete event.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: dataCollectedEvent, session_id: str | None).
        """
        self.client.on('Tracing.dataCollected', callback)
    def on_tracing_complete(self, callback: Callable[[tracingCompleteEvent, str | None], None] | None = None) -> None:
        """
    Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: tracingCompleteEvent, session_id: str | None).
        """
        self.client.on('Tracing.tracingComplete', callback)