"""CDP ServiceWorker Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import ServiceWorkerMethods
from .events.service import ServiceWorkerEvents

if TYPE_CHECKING:
    from ...service import Client

class ServiceWorker(ServiceWorkerMethods, ServiceWorkerEvents):
    """
    Access the ServiceWorker domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the ServiceWorker domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        ServiceWorkerMethods.__init__(self, client)
        ServiceWorkerEvents.__init__(self, client)