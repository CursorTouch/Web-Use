"""CDP Cast Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class CastEvents:
    """
    Events for the Cast domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Cast events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_sinks_updated(self, callback: Callable[[sinksUpdatedEvent, str | None], None] | None = None) -> None:
        """
    This is fired whenever the list of available sinks changes. A sink is a device or a software surface that you can cast to.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: sinksUpdatedEvent, session_id: str | None).
        """
        self.client.on('Cast.sinksUpdated', callback)
    def on_issue_updated(self, callback: Callable[[issueUpdatedEvent, str | None], None] | None = None) -> None:
        """
    This is fired whenever the outstanding issue/error message changes. |issueMessage| is empty if there is no issue.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: issueUpdatedEvent, session_id: str | None).
        """
        self.client.on('Cast.issueUpdated', callback)