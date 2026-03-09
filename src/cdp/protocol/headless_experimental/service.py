"""CDP HeadlessExperimental Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import HeadlessExperimentalMethods
from .events.service import HeadlessExperimentalEvents

if TYPE_CHECKING:
    from ...service import Client

class HeadlessExperimental(HeadlessExperimentalMethods, HeadlessExperimentalEvents):
    """
    This domain provides experimental commands only supported in headless mode.
    """
    def __init__(self, client: Client):
        """
        Initialize the HeadlessExperimental domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        HeadlessExperimentalMethods.__init__(self, client)
        HeadlessExperimentalEvents.__init__(self, client)