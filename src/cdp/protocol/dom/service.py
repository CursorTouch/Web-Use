"""CDP DOM Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DOMMethods
from .events.service import DOMEvents

if TYPE_CHECKING:
    from ...service import Client

class DOM(DOMMethods, DOMEvents):
    """
    This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object that has an `id`. This `id` can be used to get additional information on the Node, resolve it into the JavaScript object wrapper, etc. It is important that client receives DOM events only for the nodes that are known to the client. Backend keeps track of the nodes that were sent to the client and never sends the same node twice. It is client's responsibility to collect information about the nodes that were sent to the client. Note that `iframe` owner elements will return corresponding document elements as their child nodes.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOM domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DOMMethods.__init__(self, client)
        DOMEvents.__init__(self, client)