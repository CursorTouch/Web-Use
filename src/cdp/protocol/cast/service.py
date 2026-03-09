"""CDP Cast Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import CastMethods
from .events.service import CastEvents

if TYPE_CHECKING:
    from ...service import Client

class Cast(CastMethods, CastEvents):
    """
    A domain for interacting with Cast, Presentation API, and Remote Playback API functionalities.
    """
    def __init__(self, client: Client):
        """
        Initialize the Cast domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        CastMethods.__init__(self, client)
        CastEvents.__init__(self, client)