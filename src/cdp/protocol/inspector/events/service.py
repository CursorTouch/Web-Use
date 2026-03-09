"""CDP Inspector Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class InspectorEvents:
    """
    Events for the Inspector domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Inspector events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_detached(self, callback: Callable[[detachedEvent, str | None], None] | None = None) -> None:
        """
    Fired when remote debugging connection is about to be terminated. Contains detach reason.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: detachedEvent, session_id: str | None).
        """
        self.client.on('Inspector.detached', callback)
    def on_target_crashed(self, callback: Callable[[targetCrashedEvent, str | None], None] | None = None) -> None:
        """
    Fired when debugging target has crashed    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: targetCrashedEvent, session_id: str | None).
        """
        self.client.on('Inspector.targetCrashed', callback)
    def on_target_reloaded_after_crash(self, callback: Callable[[targetReloadedAfterCrashEvent, str | None], None] | None = None) -> None:
        """
    Fired when debugging target has reloaded after crash    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: targetReloadedAfterCrashEvent, session_id: str | None).
        """
        self.client.on('Inspector.targetReloadedAfterCrash', callback)
    def on_worker_script_loaded(self, callback: Callable[[workerScriptLoadedEvent, str | None], None] | None = None) -> None:
        """
    Fired on worker targets when main worker script and any imported scripts have been evaluated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: workerScriptLoadedEvent, session_id: str | None).
        """
        self.client.on('Inspector.workerScriptLoaded', callback)