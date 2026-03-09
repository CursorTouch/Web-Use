"""CDP Performance Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PerformanceEvents:
    """
    Events for the Performance domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Performance events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_metrics(self, callback: Callable[[metricsEvent, str | None], None] | None = None) -> None:
        """
    Current values of the metrics.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: metricsEvent, session_id: str | None).
        """
        self.client.on('Performance.metrics', callback)