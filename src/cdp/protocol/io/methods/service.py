"""CDP IO Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class IOMethods:
    """
    Methods for the IO domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the IO methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def close(self, params: closeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Close the stream, discard any temporary backing storage.    
        Args:
            params (closeParameters, optional): Parameters for the close method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the close call.
        """
        return await self.client.send(method="IO.close", params=params, session_id=session_id)
    async def read(self, params: readParameters | None = None, session_id: str | None = None) -> readReturns:
        """
    Read a chunk of the stream    
        Args:
            params (readParameters, optional): Parameters for the read method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    readReturns: The result of the read call.
        """
        return await self.client.send(method="IO.read", params=params, session_id=session_id)
    async def resolve_blob(self, params: resolveBlobParameters | None = None, session_id: str | None = None) -> resolveBlobReturns:
        """
    Return UUID of Blob object specified by a remote object id.    
        Args:
            params (resolveBlobParameters, optional): Parameters for the resolveBlob method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    resolveBlobReturns: The result of the resolveBlob call.
        """
        return await self.client.send(method="IO.resolveBlob", params=params, session_id=session_id)