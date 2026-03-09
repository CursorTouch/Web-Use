"""CDP Runtime Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import RuntimeMethods
from .events.service import RuntimeEvents

if TYPE_CHECKING:
    from ...service import Client

class Runtime(RuntimeMethods, RuntimeEvents):
    """
    Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects. Evaluation results are returned as mirror object that expose object type, string representation and unique identifier that can be used for further object reference. Original objects are maintained in memory unless they are either explicitly released or are released along with the other objects in their object group.
    """
    def __init__(self, client: Client):
        """
        Initialize the Runtime domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        RuntimeMethods.__init__(self, client)
        RuntimeEvents.__init__(self, client)