"""CDP WebAuthn Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class WebAuthnEvents:
    """
    Events for the WebAuthn domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the WebAuthn events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_credential_added(self, callback: Callable[[credentialAddedEvent, str | None], None] | None = None) -> None:
        """
    Triggered when a credential is added to an authenticator.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: credentialAddedEvent, session_id: str | None).
        """
        self.client.on('WebAuthn.credentialAdded', callback)
    def on_credential_deleted(self, callback: Callable[[credentialDeletedEvent, str | None], None] | None = None) -> None:
        """
    Triggered when a credential is deleted, e.g. through PublicKeyCredential.signalUnknownCredential().    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: credentialDeletedEvent, session_id: str | None).
        """
        self.client.on('WebAuthn.credentialDeleted', callback)
    def on_credential_updated(self, callback: Callable[[credentialUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Triggered when a credential is updated, e.g. through PublicKeyCredential.signalCurrentUserDetails().    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: credentialUpdatedEvent, session_id: str | None).
        """
        self.client.on('WebAuthn.credentialUpdated', callback)
    def on_credential_asserted(self, callback: Callable[[credentialAssertedEvent, str | None], None] | None = None) -> None:
        """
    Triggered when a credential is used in a webauthn assertion.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: credentialAssertedEvent, session_id: str | None).
        """
        self.client.on('WebAuthn.credentialAsserted', callback)