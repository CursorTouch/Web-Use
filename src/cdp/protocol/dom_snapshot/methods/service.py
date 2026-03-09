"""CDP DOMSnapshot Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DOMSnapshotMethods:
    """
    Methods for the DOMSnapshot domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMSnapshot methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables DOM snapshot agent for the given page.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="DOMSnapshot.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables DOM snapshot agent for the given page.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="DOMSnapshot.enable", params=params, session_id=session_id)
    async def capture_snapshot(self, params: captureSnapshotParameters | None = None, session_id: str | None = None) -> captureSnapshotReturns:
        """
    Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened.    
        Args:
            params (captureSnapshotParameters, optional): Parameters for the captureSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    captureSnapshotReturns: The result of the captureSnapshot call.
        """
        return await self.client.send(method="DOMSnapshot.captureSnapshot", params=params, session_id=session_id)