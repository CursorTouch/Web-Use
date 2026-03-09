"""CDP Animation Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import AnimationMethods
from .events.service import AnimationEvents

if TYPE_CHECKING:
    from ...service import Client

class Animation(AnimationMethods, AnimationEvents):
    """
    Access the Animation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Animation domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        AnimationMethods.__init__(self, client)
        AnimationEvents.__init__(self, client)