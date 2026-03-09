"""CDP CacheStorage Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class CacheStorageMethods:
    """
    Methods for the CacheStorage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the CacheStorage methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def delete_cache(self, params: deleteCacheParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes a cache.    
        Args:
            params (deleteCacheParameters, optional): Parameters for the deleteCache method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteCache call.
        """
        return await self.client.send(method="CacheStorage.deleteCache", params=params, session_id=session_id)
    async def delete_entry(self, params: deleteEntryParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes a cache entry.    
        Args:
            params (deleteEntryParameters, optional): Parameters for the deleteEntry method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteEntry call.
        """
        return await self.client.send(method="CacheStorage.deleteEntry", params=params, session_id=session_id)
    async def request_cache_names(self, params: requestCacheNamesParameters | None = None, session_id: str | None = None) -> requestCacheNamesReturns:
        """
    Requests cache names.    
        Args:
            params (requestCacheNamesParameters, optional): Parameters for the requestCacheNames method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestCacheNamesReturns: The result of the requestCacheNames call.
        """
        return await self.client.send(method="CacheStorage.requestCacheNames", params=params, session_id=session_id)
    async def request_cached_response(self, params: requestCachedResponseParameters | None = None, session_id: str | None = None) -> requestCachedResponseReturns:
        """
    Fetches cache entry.    
        Args:
            params (requestCachedResponseParameters, optional): Parameters for the requestCachedResponse method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestCachedResponseReturns: The result of the requestCachedResponse call.
        """
        return await self.client.send(method="CacheStorage.requestCachedResponse", params=params, session_id=session_id)
    async def request_entries(self, params: requestEntriesParameters | None = None, session_id: str | None = None) -> requestEntriesReturns:
        """
    Requests data from cache.    
        Args:
            params (requestEntriesParameters, optional): Parameters for the requestEntries method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestEntriesReturns: The result of the requestEntries call.
        """
        return await self.client.send(method="CacheStorage.requestEntries", params=params, session_id=session_id)