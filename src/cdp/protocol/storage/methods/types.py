"""CDP Storage Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.browser.types import BrowserContextID
    from cdp.protocol.network.types import Cookie
    from cdp.protocol.network.types import CookieParam
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.storage.types import RelatedWebsiteSet
    from cdp.protocol.storage.types import SerializedStorageKey
    from cdp.protocol.storage.types import SharedStorageEntry
    from cdp.protocol.storage.types import SharedStorageMetadata
    from cdp.protocol.storage.types import StorageBucket
    from cdp.protocol.storage.types import TrustTokens
    from cdp.protocol.storage.types import UsageForType

class getStorageKeyParameters(TypedDict, total=False):
    frameId: NotRequired[FrameId]
class clearDataForOriginParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
    storageTypes: str
    """Comma separated list of StorageType to clear."""
class clearDataForStorageKeyParameters(TypedDict, total=True):
    storageKey: str
    """Storage key."""
    storageTypes: str
    """Comma separated list of StorageType to clear."""
class getCookiesParameters(TypedDict, total=False):
    browserContextId: NotRequired[BrowserContextID]
    """Browser context to use when called on the browser endpoint."""
class setCookiesParameters(TypedDict, total=True):
    cookies: List[CookieParam]
    """Cookies to be set."""
    browserContextId: NotRequired[BrowserContextID]
    """Browser context to use when called on the browser endpoint."""
class clearCookiesParameters(TypedDict, total=False):
    browserContextId: NotRequired[BrowserContextID]
    """Browser context to use when called on the browser endpoint."""
class getUsageAndQuotaParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
class overrideQuotaForOriginParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
    quotaSize: NotRequired[float]
    """The quota size (in bytes) to override the original quota with. If this is called multiple times, the overridden quota will be equal to the quotaSize provided in the final call. If this is called without specifying a quotaSize, the quota will be reset to the default value for the specified origin. If this is called multiple times with different origins, the override will be maintained for each origin until it is disabled (called without a quotaSize)."""
class trackCacheStorageForOriginParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
class trackCacheStorageForStorageKeyParameters(TypedDict, total=True):
    storageKey: str
    """Storage key."""
class trackIndexedDBForOriginParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
class trackIndexedDBForStorageKeyParameters(TypedDict, total=True):
    storageKey: str
    """Storage key."""
class untrackCacheStorageForOriginParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
class untrackCacheStorageForStorageKeyParameters(TypedDict, total=True):
    storageKey: str
    """Storage key."""
class untrackIndexedDBForOriginParameters(TypedDict, total=True):
    origin: str
    """Security origin."""
class untrackIndexedDBForStorageKeyParameters(TypedDict, total=True):
    storageKey: str
    """Storage key."""

class clearTrustTokensParameters(TypedDict, total=True):
    issuerOrigin: str
class getInterestGroupDetailsParameters(TypedDict, total=True):
    ownerOrigin: str
    name: str
class setInterestGroupTrackingParameters(TypedDict, total=True):
    enable: bool
class setInterestGroupAuctionTrackingParameters(TypedDict, total=True):
    enable: bool
class getSharedStorageMetadataParameters(TypedDict, total=True):
    ownerOrigin: str
class getSharedStorageEntriesParameters(TypedDict, total=True):
    ownerOrigin: str
class setSharedStorageEntryParameters(TypedDict, total=True):
    ownerOrigin: str
    key: str
    value: str
    ignoreIfPresent: NotRequired[bool]
    """If ignoreIfPresent is included and true, then only sets the entry if key doesn't already exist."""
class deleteSharedStorageEntryParameters(TypedDict, total=True):
    ownerOrigin: str
    key: str
class clearSharedStorageEntriesParameters(TypedDict, total=True):
    ownerOrigin: str
class resetSharedStorageBudgetParameters(TypedDict, total=True):
    ownerOrigin: str
class setSharedStorageTrackingParameters(TypedDict, total=True):
    enable: bool
class setStorageBucketTrackingParameters(TypedDict, total=True):
    storageKey: str
    enable: bool
class deleteStorageBucketParameters(TypedDict, total=True):
    bucket: StorageBucket

class setAttributionReportingLocalTestingModeParameters(TypedDict, total=True):
    enabled: bool
    """If enabled, noise is suppressed and reports are sent immediately."""
class setAttributionReportingTrackingParameters(TypedDict, total=True):
    enable: bool


class getAffectedUrlsForThirdPartyCookieMetadataParameters(TypedDict, total=True):
    firstPartyUrl: str
    """The URL of the page currently being visited."""
    thirdPartyUrls: List[str]
    """The list of embedded resource URLs from the page."""
class setProtectedAudienceKAnonymityParameters(TypedDict, total=True):
    owner: str
    name: str
    hashes: List[str]
class getStorageKeyReturns(TypedDict):
    storageKey: SerializedStorageKey


class getCookiesReturns(TypedDict):
    cookies: List[Cookie]
    """Array of cookie objects."""


class getUsageAndQuotaReturns(TypedDict):
    usage: float
    """Storage usage (bytes)."""
    quota: float
    """Storage quota (bytes)."""
    overrideActive: bool
    """Whether or not the origin has an active storage quota override"""
    usageBreakdown: List[UsageForType]
    """Storage usage per type (bytes)."""









class getTrustTokensReturns(TypedDict):
    tokens: List[TrustTokens]
class clearTrustTokensReturns(TypedDict):
    didDeleteTokens: bool
    """True if any tokens were deleted, false otherwise."""
class getInterestGroupDetailsReturns(TypedDict):
    details: Dict[str, Any]
    """This largely corresponds to: https://wicg.github.io/turtledove/#dictdef-generatebidinterestgroup but has absolute expirationTime instead of relative lifetimeMs and also adds joiningOrigin."""


class getSharedStorageMetadataReturns(TypedDict):
    metadata: SharedStorageMetadata
class getSharedStorageEntriesReturns(TypedDict):
    entries: List[SharedStorageEntry]







class runBounceTrackingMitigationsReturns(TypedDict):
    deletedSites: List[str]


class sendPendingAttributionReportsReturns(TypedDict):
    numSent: int
    """The number of reports that were sent."""
class getRelatedWebsiteSetsReturns(TypedDict):
    sets: List[RelatedWebsiteSet]
class getAffectedUrlsForThirdPartyCookieMetadataReturns(TypedDict):
    matchedUrls: List[str]
    """Array of matching URLs. If there is a primary pattern match for the first- party URL, only the first-party URL is returned in the array."""