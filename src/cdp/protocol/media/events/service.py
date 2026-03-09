"""CDP Media Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class MediaEvents:
    """
    Events for the Media domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Media events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_player_properties_changed(self, callback: Callable[[playerPropertiesChangedEvent, str | None], None] | None = None) -> None:
        """
    This can be called multiple times, and can be used to set / override / remove player properties. A null propValue indicates removal.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: playerPropertiesChangedEvent, session_id: str | None).
        """
        self.client.on('Media.playerPropertiesChanged', callback)
    def on_player_events_added(self, callback: Callable[[playerEventsAddedEvent, str | None], None] | None = None) -> None:
        """
    Send events as a list, allowing them to be batched on the browser for less congestion. If batched, events must ALWAYS be in chronological order.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: playerEventsAddedEvent, session_id: str | None).
        """
        self.client.on('Media.playerEventsAdded', callback)
    def on_player_messages_logged(self, callback: Callable[[playerMessagesLoggedEvent, str | None], None] | None = None) -> None:
        """
    Send a list of any messages that need to be delivered.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: playerMessagesLoggedEvent, session_id: str | None).
        """
        self.client.on('Media.playerMessagesLogged', callback)
    def on_player_errors_raised(self, callback: Callable[[playerErrorsRaisedEvent, str | None], None] | None = None) -> None:
        """
    Send a list of any errors that need to be delivered.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: playerErrorsRaisedEvent, session_id: str | None).
        """
        self.client.on('Media.playerErrorsRaised', callback)
    def on_player_created(self, callback: Callable[[playerCreatedEvent, str | None], None] | None = None) -> None:
        """
    Called whenever a player is created, or when a new agent joins and receives a list of active players. If an agent is restored, it will receive one event for each active player.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: playerCreatedEvent, session_id: str | None).
        """
        self.client.on('Media.playerCreated', callback)