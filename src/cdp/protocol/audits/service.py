"""CDP Audits Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import AuditsMethods
from .events.service import AuditsEvents

if TYPE_CHECKING:
    from ...service import Client

class Audits(AuditsMethods, AuditsEvents):
    """
    Audits domain allows investigation of page violations and possible improvements.
    """
    def __init__(self, client: Client):
        """
        Initialize the Audits domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        AuditsMethods.__init__(self, client)
        AuditsEvents.__init__(self, client)