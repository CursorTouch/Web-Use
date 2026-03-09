"""CDP IndexedDB Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class IndexedDBMethods:
    """
    Methods for the IndexedDB domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the IndexedDB methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def clear_object_store(self, params: clearObjectStoreParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears all entries from an object store.    
        Args:
            params (clearObjectStoreParameters, optional): Parameters for the clearObjectStore method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearObjectStore call.
        """
        return await self.client.send(method="IndexedDB.clearObjectStore", params=params, session_id=session_id)
    async def delete_database(self, params: deleteDatabaseParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes a database.    
        Args:
            params (deleteDatabaseParameters, optional): Parameters for the deleteDatabase method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteDatabase call.
        """
        return await self.client.send(method="IndexedDB.deleteDatabase", params=params, session_id=session_id)
    async def delete_object_store_entries(self, params: deleteObjectStoreEntriesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Delete a range of entries from an object store    
        Args:
            params (deleteObjectStoreEntriesParameters, optional): Parameters for the deleteObjectStoreEntries method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteObjectStoreEntries call.
        """
        return await self.client.send(method="IndexedDB.deleteObjectStoreEntries", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables events from backend.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="IndexedDB.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables events from backend.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="IndexedDB.enable", params=params, session_id=session_id)
    async def request_data(self, params: requestDataParameters | None = None, session_id: str | None = None) -> requestDataReturns:
        """
    Requests data from object store or index.    
        Args:
            params (requestDataParameters, optional): Parameters for the requestData method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestDataReturns: The result of the requestData call.
        """
        return await self.client.send(method="IndexedDB.requestData", params=params, session_id=session_id)
    async def get_metadata(self, params: getMetadataParameters | None = None, session_id: str | None = None) -> getMetadataReturns:
        """
    Gets metadata of an object store.    
        Args:
            params (getMetadataParameters, optional): Parameters for the getMetadata method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getMetadataReturns: The result of the getMetadata call.
        """
        return await self.client.send(method="IndexedDB.getMetadata", params=params, session_id=session_id)
    async def request_database(self, params: requestDatabaseParameters | None = None, session_id: str | None = None) -> requestDatabaseReturns:
        """
    Requests database with given name in given frame.    
        Args:
            params (requestDatabaseParameters, optional): Parameters for the requestDatabase method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestDatabaseReturns: The result of the requestDatabase call.
        """
        return await self.client.send(method="IndexedDB.requestDatabase", params=params, session_id=session_id)
    async def request_database_names(self, params: requestDatabaseNamesParameters | None = None, session_id: str | None = None) -> requestDatabaseNamesReturns:
        """
    Requests database names for given security origin.    
        Args:
            params (requestDatabaseNamesParameters, optional): Parameters for the requestDatabaseNames method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestDatabaseNamesReturns: The result of the requestDatabaseNames call.
        """
        return await self.client.send(method="IndexedDB.requestDatabaseNames", params=params, session_id=session_id)