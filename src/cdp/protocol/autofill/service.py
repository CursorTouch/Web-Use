"""CDP Autofill Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import AutofillMethods
from .events.service import AutofillEvents

if TYPE_CHECKING:
    from ...service import Client

class Autofill(AutofillMethods, AutofillEvents):
    """
    Defines commands and events for Autofill.
    """
    def __init__(self, client: Client):
        """
        Initialize the Autofill domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        AutofillMethods.__init__(self, client)
        AutofillEvents.__init__(self, client)