"""CDP Preload Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PreloadEvents:
    """
    Events for the Preload domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Preload events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_rule_set_updated(self, callback: Callable[[ruleSetUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Upsert. Currently, it is only emitted when a rule set added.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: ruleSetUpdatedEvent, session_id: str | None).
        """
        self.client.on('Preload.ruleSetUpdated', callback)
    def on_rule_set_removed(self, callback: Callable[[ruleSetRemovedEvent, str | None], None] | None = None) -> None:
        """
    No description available for ruleSetRemoved.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: ruleSetRemovedEvent, session_id: str | None).
        """
        self.client.on('Preload.ruleSetRemoved', callback)
    def on_preload_enabled_state_updated(self, callback: Callable[[preloadEnabledStateUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Fired when a preload enabled state is updated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: preloadEnabledStateUpdatedEvent, session_id: str | None).
        """
        self.client.on('Preload.preloadEnabledStateUpdated', callback)
    def on_prefetch_status_updated(self, callback: Callable[[prefetchStatusUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Fired when a prefetch attempt is updated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: prefetchStatusUpdatedEvent, session_id: str | None).
        """
        self.client.on('Preload.prefetchStatusUpdated', callback)
    def on_prerender_status_updated(self, callback: Callable[[prerenderStatusUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Fired when a prerender attempt is updated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: prerenderStatusUpdatedEvent, session_id: str | None).
        """
        self.client.on('Preload.prerenderStatusUpdated', callback)
    def on_preloading_attempt_sources_updated(self, callback: Callable[[preloadingAttemptSourcesUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Send a list of sources for all preloading attempts in a document.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: preloadingAttemptSourcesUpdatedEvent, session_id: str | None).
        """
        self.client.on('Preload.preloadingAttemptSourcesUpdated', callback)