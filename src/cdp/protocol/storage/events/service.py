"""CDP Storage Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class StorageEvents:
    """
    Events for the Storage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Storage events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_cache_storage_content_updated(self, callback: Callable[[cacheStorageContentUpdatedEvent, str | None], None] | None = None) -> None:
        """
    A cache's contents have been modified.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: cacheStorageContentUpdatedEvent, session_id: str | None).
        """
        self.client.on('Storage.cacheStorageContentUpdated', callback)
    def on_cache_storage_list_updated(self, callback: Callable[[cacheStorageListUpdatedEvent, str | None], None] | None = None) -> None:
        """
    A cache has been added/deleted.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: cacheStorageListUpdatedEvent, session_id: str | None).
        """
        self.client.on('Storage.cacheStorageListUpdated', callback)
    def on_indexed_db_content_updated(self, callback: Callable[[indexedDBContentUpdatedEvent, str | None], None] | None = None) -> None:
        """
    The origin's IndexedDB object store has been modified.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: indexedDBContentUpdatedEvent, session_id: str | None).
        """
        self.client.on('Storage.indexedDBContentUpdated', callback)
    def on_indexed_db_list_updated(self, callback: Callable[[indexedDBListUpdatedEvent, str | None], None] | None = None) -> None:
        """
    The origin's IndexedDB database list has been modified.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: indexedDBListUpdatedEvent, session_id: str | None).
        """
        self.client.on('Storage.indexedDBListUpdated', callback)
    def on_interest_group_accessed(self, callback: Callable[[interestGroupAccessedEvent, str | None], None] | None = None) -> None:
        """
    One of the interest groups was accessed. Note that these events are global to all targets sharing an interest group store.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: interestGroupAccessedEvent, session_id: str | None).
        """
        self.client.on('Storage.interestGroupAccessed', callback)
    def on_interest_group_auction_event_occurred(self, callback: Callable[[interestGroupAuctionEventOccurredEvent, str | None], None] | None = None) -> None:
        """
    An auction involving interest groups is taking place. These events are target-specific.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: interestGroupAuctionEventOccurredEvent, session_id: str | None).
        """
        self.client.on('Storage.interestGroupAuctionEventOccurred', callback)
    def on_interest_group_auction_network_request_created(self, callback: Callable[[interestGroupAuctionNetworkRequestCreatedEvent, str | None], None] | None = None) -> None:
        """
    Specifies which auctions a particular network fetch may be related to, and in what role. Note that it is not ordered with respect to Network.requestWillBeSent (but will happen before loadingFinished loadingFailed).    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: interestGroupAuctionNetworkRequestCreatedEvent, session_id: str | None).
        """
        self.client.on('Storage.interestGroupAuctionNetworkRequestCreated', callback)
    def on_shared_storage_accessed(self, callback: Callable[[sharedStorageAccessedEvent, str | None], None] | None = None) -> None:
        """
    Shared storage was accessed by the associated page. The following parameters are included in all events.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: sharedStorageAccessedEvent, session_id: str | None).
        """
        self.client.on('Storage.sharedStorageAccessed', callback)
    def on_shared_storage_worklet_operation_execution_finished(self, callback: Callable[[sharedStorageWorkletOperationExecutionFinishedEvent, str | None], None] | None = None) -> None:
        """
    A shared storage run or selectURL operation finished its execution. The following parameters are included in all events.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: sharedStorageWorkletOperationExecutionFinishedEvent, session_id: str | None).
        """
        self.client.on('Storage.sharedStorageWorkletOperationExecutionFinished', callback)
    def on_storage_bucket_created_or_updated(self, callback: Callable[[storageBucketCreatedOrUpdatedEvent, str | None], None] | None = None) -> None:
        """
    No description available for storageBucketCreatedOrUpdated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: storageBucketCreatedOrUpdatedEvent, session_id: str | None).
        """
        self.client.on('Storage.storageBucketCreatedOrUpdated', callback)
    def on_storage_bucket_deleted(self, callback: Callable[[storageBucketDeletedEvent, str | None], None] | None = None) -> None:
        """
    No description available for storageBucketDeleted.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: storageBucketDeletedEvent, session_id: str | None).
        """
        self.client.on('Storage.storageBucketDeleted', callback)
    def on_attribution_reporting_source_registered(self, callback: Callable[[attributionReportingSourceRegisteredEvent, str | None], None] | None = None) -> None:
        """
    No description available for attributionReportingSourceRegistered.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: attributionReportingSourceRegisteredEvent, session_id: str | None).
        """
        self.client.on('Storage.attributionReportingSourceRegistered', callback)
    def on_attribution_reporting_trigger_registered(self, callback: Callable[[attributionReportingTriggerRegisteredEvent, str | None], None] | None = None) -> None:
        """
    No description available for attributionReportingTriggerRegistered.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: attributionReportingTriggerRegisteredEvent, session_id: str | None).
        """
        self.client.on('Storage.attributionReportingTriggerRegistered', callback)
    def on_attribution_reporting_report_sent(self, callback: Callable[[attributionReportingReportSentEvent, str | None], None] | None = None) -> None:
        """
    No description available for attributionReportingReportSent.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: attributionReportingReportSentEvent, session_id: str | None).
        """
        self.client.on('Storage.attributionReportingReportSent', callback)
    def on_attribution_reporting_verbose_debug_report_sent(self, callback: Callable[[attributionReportingVerboseDebugReportSentEvent, str | None], None] | None = None) -> None:
        """
    No description available for attributionReportingVerboseDebugReportSent.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: attributionReportingVerboseDebugReportSentEvent, session_id: str | None).
        """
        self.client.on('Storage.attributionReportingVerboseDebugReportSent', callback)