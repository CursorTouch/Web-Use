"""CDP ServiceWorker Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class ServiceWorkerEvents:
    """
    Events for the ServiceWorker domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the ServiceWorker events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_worker_error_reported(self, callback: Callable[[workerErrorReportedEvent, str | None], None] | None = None) -> None:
        """
    No description available for workerErrorReported.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: workerErrorReportedEvent, session_id: str | None).
        """
        self.client.on('ServiceWorker.workerErrorReported', callback)
    def on_worker_registration_updated(self, callback: Callable[[workerRegistrationUpdatedEvent, str | None], None] | None = None) -> None:
        """
    No description available for workerRegistrationUpdated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: workerRegistrationUpdatedEvent, session_id: str | None).
        """
        self.client.on('ServiceWorker.workerRegistrationUpdated', callback)
    def on_worker_version_updated(self, callback: Callable[[workerVersionUpdatedEvent, str | None], None] | None = None) -> None:
        """
    No description available for workerVersionUpdated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: workerVersionUpdatedEvent, session_id: str | None).
        """
        self.client.on('ServiceWorker.workerVersionUpdated', callback)