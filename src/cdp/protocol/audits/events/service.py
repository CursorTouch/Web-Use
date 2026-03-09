"""CDP Audits Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AuditsEvents:
    """
    Events for the Audits domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Audits events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_issue_added(self, callback: Callable[[issueAddedEvent, str | None], None] | None = None) -> None:
        """
    No description available for issueAdded.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: issueAddedEvent, session_id: str | None).
        """
        self.client.on('Audits.issueAdded', callback)