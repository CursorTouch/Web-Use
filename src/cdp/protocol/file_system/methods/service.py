"""CDP FileSystem Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class FileSystemMethods:
    """
    Methods for the FileSystem domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the FileSystem methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def get_directory(self, params: getDirectoryParameters | None = None, session_id: str | None = None) -> getDirectoryReturns:
        """
    No description available for getDirectory.    
        Args:
            params (getDirectoryParameters, optional): Parameters for the getDirectory method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getDirectoryReturns: The result of the getDirectory call.
        """
        return await self.client.send(method="FileSystem.getDirectory", params=params, session_id=session_id)