"""CDP Autofill Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AutofillEvents:
    """
    Events for the Autofill domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Autofill events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_address_form_filled(self, callback: Callable[[addressFormFilledEvent, str | None], None] | None = None) -> None:
        """
    Emitted when an address form is filled.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: addressFormFilledEvent, session_id: str | None).
        """
        self.client.on('Autofill.addressFormFilled', callback)