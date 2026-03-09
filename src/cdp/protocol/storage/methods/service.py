"""CDP Storage Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class StorageMethods:
    """
    Methods for the Storage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Storage methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def get_storage_key(self, params: getStorageKeyParameters | None = None, session_id: str | None = None) -> getStorageKeyReturns:
        """
    Returns storage key for the given frame. If no frame ID is provided, the storage key of the target executing this command is returned.    
        Args:
            params (getStorageKeyParameters, optional): Parameters for the getStorageKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getStorageKeyReturns: The result of the getStorageKey call.
        """
        return await self.client.send(method="Storage.getStorageKey", params=params, session_id=session_id)
    async def clear_data_for_origin(self, params: clearDataForOriginParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears storage for origin.    
        Args:
            params (clearDataForOriginParameters, optional): Parameters for the clearDataForOrigin method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearDataForOrigin call.
        """
        return await self.client.send(method="Storage.clearDataForOrigin", params=params, session_id=session_id)
    async def clear_data_for_storage_key(self, params: clearDataForStorageKeyParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears storage for storage key.    
        Args:
            params (clearDataForStorageKeyParameters, optional): Parameters for the clearDataForStorageKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearDataForStorageKey call.
        """
        return await self.client.send(method="Storage.clearDataForStorageKey", params=params, session_id=session_id)
    async def get_cookies(self, params: getCookiesParameters | None = None, session_id: str | None = None) -> getCookiesReturns:
        """
    Returns all browser cookies.    
        Args:
            params (getCookiesParameters, optional): Parameters for the getCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCookiesReturns: The result of the getCookies call.
        """
        return await self.client.send(method="Storage.getCookies", params=params, session_id=session_id)
    async def set_cookies(self, params: setCookiesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets given cookies.    
        Args:
            params (setCookiesParameters, optional): Parameters for the setCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCookies call.
        """
        return await self.client.send(method="Storage.setCookies", params=params, session_id=session_id)
    async def clear_cookies(self, params: clearCookiesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears cookies.    
        Args:
            params (clearCookiesParameters, optional): Parameters for the clearCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearCookies call.
        """
        return await self.client.send(method="Storage.clearCookies", params=params, session_id=session_id)
    async def get_usage_and_quota(self, params: getUsageAndQuotaParameters | None = None, session_id: str | None = None) -> getUsageAndQuotaReturns:
        """
    Returns usage and quota in bytes.    
        Args:
            params (getUsageAndQuotaParameters, optional): Parameters for the getUsageAndQuota method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getUsageAndQuotaReturns: The result of the getUsageAndQuota call.
        """
        return await self.client.send(method="Storage.getUsageAndQuota", params=params, session_id=session_id)
    async def override_quota_for_origin(self, params: overrideQuotaForOriginParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Override quota for the specified origin    
        Args:
            params (overrideQuotaForOriginParameters, optional): Parameters for the overrideQuotaForOrigin method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the overrideQuotaForOrigin call.
        """
        return await self.client.send(method="Storage.overrideQuotaForOrigin", params=params, session_id=session_id)
    async def track_cache_storage_for_origin(self, params: trackCacheStorageForOriginParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Registers origin to be notified when an update occurs to its cache storage list.    
        Args:
            params (trackCacheStorageForOriginParameters, optional): Parameters for the trackCacheStorageForOrigin method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the trackCacheStorageForOrigin call.
        """
        return await self.client.send(method="Storage.trackCacheStorageForOrigin", params=params, session_id=session_id)
    async def track_cache_storage_for_storage_key(self, params: trackCacheStorageForStorageKeyParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Registers storage key to be notified when an update occurs to its cache storage list.    
        Args:
            params (trackCacheStorageForStorageKeyParameters, optional): Parameters for the trackCacheStorageForStorageKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the trackCacheStorageForStorageKey call.
        """
        return await self.client.send(method="Storage.trackCacheStorageForStorageKey", params=params, session_id=session_id)
    async def track_indexed_db_for_origin(self, params: trackIndexedDBForOriginParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Registers origin to be notified when an update occurs to its IndexedDB.    
        Args:
            params (trackIndexedDBForOriginParameters, optional): Parameters for the trackIndexedDBForOrigin method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the trackIndexedDBForOrigin call.
        """
        return await self.client.send(method="Storage.trackIndexedDBForOrigin", params=params, session_id=session_id)
    async def track_indexed_db_for_storage_key(self, params: trackIndexedDBForStorageKeyParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Registers storage key to be notified when an update occurs to its IndexedDB.    
        Args:
            params (trackIndexedDBForStorageKeyParameters, optional): Parameters for the trackIndexedDBForStorageKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the trackIndexedDBForStorageKey call.
        """
        return await self.client.send(method="Storage.trackIndexedDBForStorageKey", params=params, session_id=session_id)
    async def untrack_cache_storage_for_origin(self, params: untrackCacheStorageForOriginParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Unregisters origin from receiving notifications for cache storage.    
        Args:
            params (untrackCacheStorageForOriginParameters, optional): Parameters for the untrackCacheStorageForOrigin method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the untrackCacheStorageForOrigin call.
        """
        return await self.client.send(method="Storage.untrackCacheStorageForOrigin", params=params, session_id=session_id)
    async def untrack_cache_storage_for_storage_key(self, params: untrackCacheStorageForStorageKeyParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Unregisters storage key from receiving notifications for cache storage.    
        Args:
            params (untrackCacheStorageForStorageKeyParameters, optional): Parameters for the untrackCacheStorageForStorageKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the untrackCacheStorageForStorageKey call.
        """
        return await self.client.send(method="Storage.untrackCacheStorageForStorageKey", params=params, session_id=session_id)
    async def untrack_indexed_db_for_origin(self, params: untrackIndexedDBForOriginParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Unregisters origin from receiving notifications for IndexedDB.    
        Args:
            params (untrackIndexedDBForOriginParameters, optional): Parameters for the untrackIndexedDBForOrigin method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the untrackIndexedDBForOrigin call.
        """
        return await self.client.send(method="Storage.untrackIndexedDBForOrigin", params=params, session_id=session_id)
    async def untrack_indexed_db_for_storage_key(self, params: untrackIndexedDBForStorageKeyParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Unregisters storage key from receiving notifications for IndexedDB.    
        Args:
            params (untrackIndexedDBForStorageKeyParameters, optional): Parameters for the untrackIndexedDBForStorageKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the untrackIndexedDBForStorageKey call.
        """
        return await self.client.send(method="Storage.untrackIndexedDBForStorageKey", params=params, session_id=session_id)
    async def get_trust_tokens(self, params: getTrustTokensParameters | None = None, session_id: str | None = None) -> getTrustTokensReturns:
        """
    Returns the number of stored Trust Tokens per issuer for the current browsing context.    
        Args:
            params (getTrustTokensParameters, optional): Parameters for the getTrustTokens method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getTrustTokensReturns: The result of the getTrustTokens call.
        """
        return await self.client.send(method="Storage.getTrustTokens", params=params, session_id=session_id)
    async def clear_trust_tokens(self, params: clearTrustTokensParameters | None = None, session_id: str | None = None) -> clearTrustTokensReturns:
        """
    Removes all Trust Tokens issued by the provided issuerOrigin. Leaves other stored data, including the issuer's Redemption Records, intact.    
        Args:
            params (clearTrustTokensParameters, optional): Parameters for the clearTrustTokens method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    clearTrustTokensReturns: The result of the clearTrustTokens call.
        """
        return await self.client.send(method="Storage.clearTrustTokens", params=params, session_id=session_id)
    async def get_interest_group_details(self, params: getInterestGroupDetailsParameters | None = None, session_id: str | None = None) -> getInterestGroupDetailsReturns:
        """
    Gets details for a named interest group.    
        Args:
            params (getInterestGroupDetailsParameters, optional): Parameters for the getInterestGroupDetails method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getInterestGroupDetailsReturns: The result of the getInterestGroupDetails call.
        """
        return await self.client.send(method="Storage.getInterestGroupDetails", params=params, session_id=session_id)
    async def set_interest_group_tracking(self, params: setInterestGroupTrackingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables/Disables issuing of interestGroupAccessed events.    
        Args:
            params (setInterestGroupTrackingParameters, optional): Parameters for the setInterestGroupTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setInterestGroupTracking call.
        """
        return await self.client.send(method="Storage.setInterestGroupTracking", params=params, session_id=session_id)
    async def set_interest_group_auction_tracking(self, params: setInterestGroupAuctionTrackingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables/Disables issuing of interestGroupAuctionEventOccurred and interestGroupAuctionNetworkRequestCreated.    
        Args:
            params (setInterestGroupAuctionTrackingParameters, optional): Parameters for the setInterestGroupAuctionTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setInterestGroupAuctionTracking call.
        """
        return await self.client.send(method="Storage.setInterestGroupAuctionTracking", params=params, session_id=session_id)
    async def get_shared_storage_metadata(self, params: getSharedStorageMetadataParameters | None = None, session_id: str | None = None) -> getSharedStorageMetadataReturns:
        """
    Gets metadata for an origin's shared storage.    
        Args:
            params (getSharedStorageMetadataParameters, optional): Parameters for the getSharedStorageMetadata method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getSharedStorageMetadataReturns: The result of the getSharedStorageMetadata call.
        """
        return await self.client.send(method="Storage.getSharedStorageMetadata", params=params, session_id=session_id)
    async def get_shared_storage_entries(self, params: getSharedStorageEntriesParameters | None = None, session_id: str | None = None) -> getSharedStorageEntriesReturns:
        """
    Gets the entries in an given origin's shared storage.    
        Args:
            params (getSharedStorageEntriesParameters, optional): Parameters for the getSharedStorageEntries method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getSharedStorageEntriesReturns: The result of the getSharedStorageEntries call.
        """
        return await self.client.send(method="Storage.getSharedStorageEntries", params=params, session_id=session_id)
    async def set_shared_storage_entry(self, params: setSharedStorageEntryParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets entry with `key` and `value` for a given origin's shared storage.    
        Args:
            params (setSharedStorageEntryParameters, optional): Parameters for the setSharedStorageEntry method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSharedStorageEntry call.
        """
        return await self.client.send(method="Storage.setSharedStorageEntry", params=params, session_id=session_id)
    async def delete_shared_storage_entry(self, params: deleteSharedStorageEntryParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes entry for `key` (if it exists) for a given origin's shared storage.    
        Args:
            params (deleteSharedStorageEntryParameters, optional): Parameters for the deleteSharedStorageEntry method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteSharedStorageEntry call.
        """
        return await self.client.send(method="Storage.deleteSharedStorageEntry", params=params, session_id=session_id)
    async def clear_shared_storage_entries(self, params: clearSharedStorageEntriesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears all entries for a given origin's shared storage.    
        Args:
            params (clearSharedStorageEntriesParameters, optional): Parameters for the clearSharedStorageEntries method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearSharedStorageEntries call.
        """
        return await self.client.send(method="Storage.clearSharedStorageEntries", params=params, session_id=session_id)
    async def reset_shared_storage_budget(self, params: resetSharedStorageBudgetParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Resets the budget for `ownerOrigin` by clearing all budget withdrawals.    
        Args:
            params (resetSharedStorageBudgetParameters, optional): Parameters for the resetSharedStorageBudget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the resetSharedStorageBudget call.
        """
        return await self.client.send(method="Storage.resetSharedStorageBudget", params=params, session_id=session_id)
    async def set_shared_storage_tracking(self, params: setSharedStorageTrackingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables/disables issuing of sharedStorageAccessed events.    
        Args:
            params (setSharedStorageTrackingParameters, optional): Parameters for the setSharedStorageTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSharedStorageTracking call.
        """
        return await self.client.send(method="Storage.setSharedStorageTracking", params=params, session_id=session_id)
    async def set_storage_bucket_tracking(self, params: setStorageBucketTrackingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set tracking for a storage key's buckets.    
        Args:
            params (setStorageBucketTrackingParameters, optional): Parameters for the setStorageBucketTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setStorageBucketTracking call.
        """
        return await self.client.send(method="Storage.setStorageBucketTracking", params=params, session_id=session_id)
    async def delete_storage_bucket(self, params: deleteStorageBucketParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes the Storage Bucket with the given storage key and bucket name.    
        Args:
            params (deleteStorageBucketParameters, optional): Parameters for the deleteStorageBucket method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteStorageBucket call.
        """
        return await self.client.send(method="Storage.deleteStorageBucket", params=params, session_id=session_id)
    async def run_bounce_tracking_mitigations(self, params: runBounceTrackingMitigationsParameters | None = None, session_id: str | None = None) -> runBounceTrackingMitigationsReturns:
        """
    Deletes state for sites identified as potential bounce trackers, immediately.    
        Args:
            params (runBounceTrackingMitigationsParameters, optional): Parameters for the runBounceTrackingMitigations method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    runBounceTrackingMitigationsReturns: The result of the runBounceTrackingMitigations call.
        """
        return await self.client.send(method="Storage.runBounceTrackingMitigations", params=params, session_id=session_id)
    async def set_attribution_reporting_local_testing_mode(self, params: setAttributionReportingLocalTestingModeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    https://wicg.github.io/attribution-reporting-api/    
        Args:
            params (setAttributionReportingLocalTestingModeParameters, optional): Parameters for the setAttributionReportingLocalTestingMode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAttributionReportingLocalTestingMode call.
        """
        return await self.client.send(method="Storage.setAttributionReportingLocalTestingMode", params=params, session_id=session_id)
    async def set_attribution_reporting_tracking(self, params: setAttributionReportingTrackingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables/disables issuing of Attribution Reporting events.    
        Args:
            params (setAttributionReportingTrackingParameters, optional): Parameters for the setAttributionReportingTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAttributionReportingTracking call.
        """
        return await self.client.send(method="Storage.setAttributionReportingTracking", params=params, session_id=session_id)
    async def send_pending_attribution_reports(self, params: sendPendingAttributionReportsParameters | None = None, session_id: str | None = None) -> sendPendingAttributionReportsReturns:
        """
    Sends all pending Attribution Reports immediately, regardless of their scheduled report time.    
        Args:
            params (sendPendingAttributionReportsParameters, optional): Parameters for the sendPendingAttributionReports method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    sendPendingAttributionReportsReturns: The result of the sendPendingAttributionReports call.
        """
        return await self.client.send(method="Storage.sendPendingAttributionReports", params=params, session_id=session_id)
    async def get_related_website_sets(self, params: getRelatedWebsiteSetsParameters | None = None, session_id: str | None = None) -> getRelatedWebsiteSetsReturns:
        """
    Returns the effective Related Website Sets in use by this profile for the browser session. The effective Related Website Sets will not change during a browser session.    
        Args:
            params (getRelatedWebsiteSetsParameters, optional): Parameters for the getRelatedWebsiteSets method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getRelatedWebsiteSetsReturns: The result of the getRelatedWebsiteSets call.
        """
        return await self.client.send(method="Storage.getRelatedWebsiteSets", params=params, session_id=session_id)
    async def get_affected_urls_for_third_party_cookie_metadata(self, params: getAffectedUrlsForThirdPartyCookieMetadataParameters | None = None, session_id: str | None = None) -> getAffectedUrlsForThirdPartyCookieMetadataReturns:
        """
    Returns the list of URLs from a page and its embedded resources that match existing grace period URL pattern rules. https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period    
        Args:
            params (getAffectedUrlsForThirdPartyCookieMetadataParameters, optional): Parameters for the getAffectedUrlsForThirdPartyCookieMetadata method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAffectedUrlsForThirdPartyCookieMetadataReturns: The result of the getAffectedUrlsForThirdPartyCookieMetadata call.
        """
        return await self.client.send(method="Storage.getAffectedUrlsForThirdPartyCookieMetadata", params=params, session_id=session_id)
    async def set_protected_audience_k_anonymity(self, params: setProtectedAudienceKAnonymityParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setProtectedAudienceKAnonymity.    
        Args:
            params (setProtectedAudienceKAnonymityParameters, optional): Parameters for the setProtectedAudienceKAnonymity method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setProtectedAudienceKAnonymity call.
        """
        return await self.client.send(method="Storage.setProtectedAudienceKAnonymity", params=params, session_id=session_id)