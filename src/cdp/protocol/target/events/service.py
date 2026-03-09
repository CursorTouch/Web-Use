"""CDP Target Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class TargetEvents:
    """
    Events for the Target domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Target events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_attached_to_target(self, callback: Callable[[attachedToTargetEvent, str | None], None] | None = None) -> None:
        """
    Issued when attached to target because of auto-attach or `attachToTarget` command.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: attachedToTargetEvent, session_id: str | None).
        """
        self.client.on('Target.attachedToTarget', callback)
    def on_detached_from_target(self, callback: Callable[[detachedFromTargetEvent, str | None], None] | None = None) -> None:
        """
    Issued when detached from target for any reason (including `detachFromTarget` command). Can be issued multiple times per target if multiple sessions have been attached to it.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: detachedFromTargetEvent, session_id: str | None).
        """
        self.client.on('Target.detachedFromTarget', callback)
    def on_received_message_from_target(self, callback: Callable[[receivedMessageFromTargetEvent, str | None], None] | None = None) -> None:
        """
    Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event).    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: receivedMessageFromTargetEvent, session_id: str | None).
        """
        self.client.on('Target.receivedMessageFromTarget', callback)
    def on_target_created(self, callback: Callable[[targetCreatedEvent, str | None], None] | None = None) -> None:
        """
    Issued when a possible inspection target is created.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: targetCreatedEvent, session_id: str | None).
        """
        self.client.on('Target.targetCreated', callback)
    def on_target_destroyed(self, callback: Callable[[targetDestroyedEvent, str | None], None] | None = None) -> None:
        """
    Issued when a target is destroyed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: targetDestroyedEvent, session_id: str | None).
        """
        self.client.on('Target.targetDestroyed', callback)
    def on_target_crashed(self, callback: Callable[[targetCrashedEvent, str | None], None] | None = None) -> None:
        """
    Issued when a target has crashed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: targetCrashedEvent, session_id: str | None).
        """
        self.client.on('Target.targetCrashed', callback)
    def on_target_info_changed(self, callback: Callable[[targetInfoChangedEvent, str | None], None] | None = None) -> None:
        """
    Issued when some information about a target has changed. This only happens between `targetCreated` and `targetDestroyed`.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: targetInfoChangedEvent, session_id: str | None).
        """
        self.client.on('Target.targetInfoChanged', callback)