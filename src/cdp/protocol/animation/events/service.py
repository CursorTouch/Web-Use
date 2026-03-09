"""CDP Animation Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AnimationEvents:
    """
    Events for the Animation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Animation events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_animation_canceled(self, callback: Callable[[animationCanceledEvent, str | None], None] | None = None) -> None:
        """
    Event for when an animation has been cancelled.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: animationCanceledEvent, session_id: str | None).
        """
        self.client.on('Animation.animationCanceled', callback)
    def on_animation_created(self, callback: Callable[[animationCreatedEvent, str | None], None] | None = None) -> None:
        """
    Event for each animation that has been created.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: animationCreatedEvent, session_id: str | None).
        """
        self.client.on('Animation.animationCreated', callback)
    def on_animation_started(self, callback: Callable[[animationStartedEvent, str | None], None] | None = None) -> None:
        """
    Event for animation that has been started.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: animationStartedEvent, session_id: str | None).
        """
        self.client.on('Animation.animationStarted', callback)
    def on_animation_updated(self, callback: Callable[[animationUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Event for animation that has been updated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: animationUpdatedEvent, session_id: str | None).
        """
        self.client.on('Animation.animationUpdated', callback)