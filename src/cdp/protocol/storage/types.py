"""CDP Storage Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.target.types import TargetID

SerializedStorageKey = str
StorageType = Literal['cookies','file_systems','indexeddb','local_storage','shader_cache','websql','service_workers','cache_storage','interest_groups','shared_storage','storage_buckets','all','other']
"""Enum of possible storage types."""
class UsageForType(TypedDict, total=True):
    """Usage for a storage type."""
    storageType: StorageType
    """Name of storage type."""
    usage: float
    """Storage usage (bytes)."""
class TrustTokens(TypedDict, total=True):
    """Pair of issuer origin and number of available (signed, but not used) Trust Tokens from that issuer."""
    issuerOrigin: str
    count: float
InterestGroupAuctionId = str
"""Protected audience interest group auction identifier."""
InterestGroupAccessType = Literal['join','leave','update','loaded','bid','win','additionalBid','additionalBidWin','topLevelBid','topLevelAdditionalBid','clear']
"""Enum of interest group access types."""
InterestGroupAuctionEventType = Literal['started','configResolved']
"""Enum of auction events."""
InterestGroupAuctionFetchType = Literal['bidderJs','bidderWasm','sellerJs','bidderTrustedSignals','sellerTrustedSignals']
"""Enum of network fetches auctions can do."""
SharedStorageAccessScope = Literal['window','sharedStorageWorklet','protectedAudienceWorklet','header']
"""Enum of shared storage access scopes."""
SharedStorageAccessMethod = Literal['addModule','createWorklet','selectURL','run','batchUpdate','set','append','delete','clear','get','keys','values','entries','length','remainingBudget']
"""Enum of shared storage access methods."""
class SharedStorageEntry(TypedDict, total=True):
    """Struct for a single key-value pair in an origin's shared storage."""
    key: str
    value: str
class SharedStorageMetadata(TypedDict, total=True):
    """Details for an origin's shared storage."""
    creationTime: TimeSinceEpoch
    """Time when the origin's shared storage was last created."""
    length: int
    """Number of key-value pairs stored in origin's shared storage."""
    remainingBudget: float
    """Current amount of bits of entropy remaining in the navigation budget."""
    bytesUsed: int
    """Total number of bytes stored as key-value pairs in origin's shared storage."""
class SharedStoragePrivateAggregationConfig(TypedDict, total=True):
    """Represents a dictionary object passed in as privateAggregationConfig to run or selectURL."""
    filteringIdMaxBytes: int
    """Configures the maximum size allowed for filtering IDs."""
    aggregationCoordinatorOrigin: NotRequired[str]
    """The chosen aggregation service deployment."""
    contextId: NotRequired[str]
    """The context ID provided."""
    maxContributions: NotRequired[int]
    """The limit on the number of contributions in the final report."""
class SharedStorageReportingMetadata(TypedDict, total=True):
    """Pair of reporting metadata details for a candidate URL for selectURL()."""
    eventType: str
    reportingUrl: str
class SharedStorageUrlWithMetadata(TypedDict, total=True):
    """Bundles a candidate URL with its reporting metadata."""
    url: str
    """Spec of candidate URL."""
    reportingMetadata: List[SharedStorageReportingMetadata]
    """Any associated reporting metadata."""
class SharedStorageAccessParams(TypedDict, total=False):
    """Bundles the parameters for shared storage access events whose presence/absence can vary according to SharedStorageAccessType."""
    scriptSourceUrl: NotRequired[str]
    """Spec of the module script URL. Present only for SharedStorageAccessMethods: addModule and createWorklet."""
    dataOrigin: NotRequired[str]
    """String denoting "context-origin", "script-origin", or a custom origin to be used as the worklet's data origin. Present only for SharedStorageAccessMethod: createWorklet."""
    operationName: NotRequired[str]
    """Name of the registered operation to be run. Present only for SharedStorageAccessMethods: run and selectURL."""
    operationId: NotRequired[str]
    """ID of the operation call. Present only for SharedStorageAccessMethods: run and selectURL."""
    keepAlive: NotRequired[bool]
    """Whether or not to keep the worket alive for future run or selectURL calls. Present only for SharedStorageAccessMethods: run and selectURL."""
    privateAggregationConfig: NotRequired[SharedStoragePrivateAggregationConfig]
    """Configures the private aggregation options. Present only for SharedStorageAccessMethods: run and selectURL."""
    serializedData: NotRequired[str]
    """The operation's serialized data in bytes (converted to a string). Present only for SharedStorageAccessMethods: run and selectURL. TODO(crbug.com/401011862): Consider updating this parameter to binary."""
    urlsWithMetadata: NotRequired[List[SharedStorageUrlWithMetadata]]
    """Array of candidate URLs' specs, along with any associated metadata. Present only for SharedStorageAccessMethod: selectURL."""
    urnUuid: NotRequired[str]
    """Spec of the URN:UUID generated for a selectURL call. Present only for SharedStorageAccessMethod: selectURL."""
    key: NotRequired[str]
    """Key for a specific entry in an origin's shared storage. Present only for SharedStorageAccessMethods: set, append, delete, and get."""
    value: NotRequired[str]
    """Value for a specific entry in an origin's shared storage. Present only for SharedStorageAccessMethods: set and append."""
    ignoreIfPresent: NotRequired[bool]
    """Whether or not to set an entry for a key if that key is already present. Present only for SharedStorageAccessMethod: set."""
    workletOrdinal: NotRequired[int]
    """A number denoting the (0-based) order of the worklet's creation relative to all other shared storage worklets created by documents using the current storage partition. Present only for SharedStorageAccessMethods: addModule, createWorklet."""
    workletTargetId: NotRequired[TargetID]
    """Hex representation of the DevTools token used as the TargetID for the associated shared storage worklet. Present only for SharedStorageAccessMethods: addModule, createWorklet, run, selectURL, and any other SharedStorageAccessMethod when the SharedStorageAccessScope is sharedStorageWorklet."""
    withLock: NotRequired[str]
    """Name of the lock to be acquired, if present. Optionally present only for SharedStorageAccessMethods: batchUpdate, set, append, delete, and clear."""
    batchUpdateId: NotRequired[str]
    """If the method has been called as part of a batchUpdate, then this number identifies the batch to which it belongs. Optionally present only for SharedStorageAccessMethods: batchUpdate (required), set, append, delete, and clear."""
    batchSize: NotRequired[int]
    """Number of modifier methods sent in batch. Present only for SharedStorageAccessMethod: batchUpdate."""
StorageBucketsDurability = Literal['relaxed','strict']
class StorageBucket(TypedDict, total=True):
    storageKey: SerializedStorageKey
    name: NotRequired[str]
    """If not specified, it is the default bucket of the storageKey."""
class StorageBucketInfo(TypedDict, total=True):
    bucket: StorageBucket
    id: str
    expiration: TimeSinceEpoch
    quota: float
    """Storage quota (bytes)."""
    persistent: bool
    durability: StorageBucketsDurability
AttributionReportingSourceType = Literal['navigation','event']
UnsignedInt64AsBase10 = str
UnsignedInt128AsBase16 = str
SignedInt64AsBase10 = str
class AttributionReportingFilterDataEntry(TypedDict, total=True):
    key: str
    values: List[str]
class AttributionReportingFilterConfig(TypedDict, total=True):
    filterValues: List[AttributionReportingFilterDataEntry]
    lookbackWindow: NotRequired[int]
    """duration in seconds"""
class AttributionReportingFilterPair(TypedDict, total=True):
    filters: List[AttributionReportingFilterConfig]
    notFilters: List[AttributionReportingFilterConfig]
class AttributionReportingAggregationKeysEntry(TypedDict, total=True):
    key: str
    value: UnsignedInt128AsBase16
class AttributionReportingEventReportWindows(TypedDict, total=True):
    start: int
    """duration in seconds"""
    ends: List[int]
    """duration in seconds"""
AttributionReportingTriggerDataMatching = Literal['exact','modulus']
class AttributionReportingAggregatableDebugReportingData(TypedDict, total=True):
    keyPiece: UnsignedInt128AsBase16
    value: float
    """number instead of integer because not all uint32 can be represented by int"""
    types: List[str]
class AttributionReportingAggregatableDebugReportingConfig(TypedDict, total=True):
    keyPiece: UnsignedInt128AsBase16
    debugData: List[AttributionReportingAggregatableDebugReportingData]
    budget: NotRequired[float]
    """number instead of integer because not all uint32 can be represented by int, only present for source registrations"""
    aggregationCoordinatorOrigin: NotRequired[str]
class AttributionScopesData(TypedDict, total=True):
    values: List[str]
    limit: float
    """number instead of integer because not all uint32 can be represented by int"""
    maxEventStates: float
class AttributionReportingNamedBudgetDef(TypedDict, total=True):
    name: str
    budget: int
class AttributionReportingSourceRegistration(TypedDict, total=True):
    time: TimeSinceEpoch
    expiry: int
    """duration in seconds"""
    triggerData: List[float]
    """number instead of integer because not all uint32 can be represented by int"""
    eventReportWindows: AttributionReportingEventReportWindows
    aggregatableReportWindow: int
    """duration in seconds"""
    type: AttributionReportingSourceType
    sourceOrigin: str
    reportingOrigin: str
    destinationSites: List[str]
    eventId: UnsignedInt64AsBase10
    priority: SignedInt64AsBase10
    filterData: List[AttributionReportingFilterDataEntry]
    aggregationKeys: List[AttributionReportingAggregationKeysEntry]
    triggerDataMatching: AttributionReportingTriggerDataMatching
    destinationLimitPriority: SignedInt64AsBase10
    aggregatableDebugReportingConfig: AttributionReportingAggregatableDebugReportingConfig
    maxEventLevelReports: int
    namedBudgets: List[AttributionReportingNamedBudgetDef]
    debugReporting: bool
    eventLevelEpsilon: float
    debugKey: NotRequired[UnsignedInt64AsBase10]
    scopesData: NotRequired[AttributionScopesData]
AttributionReportingSourceRegistrationResult = Literal['success','internalError','insufficientSourceCapacity','insufficientUniqueDestinationCapacity','excessiveReportingOrigins','prohibitedByBrowserPolicy','successNoised','destinationReportingLimitReached','destinationGlobalLimitReached','destinationBothLimitsReached','reportingOriginsPerSiteLimitReached','exceedsMaxChannelCapacity','exceedsMaxScopesChannelCapacity','exceedsMaxTriggerStateCardinality','exceedsMaxEventStatesLimit','destinationPerDayReportingLimitReached']
AttributionReportingSourceRegistrationTimeConfig = Literal['include','exclude']
class AttributionReportingAggregatableValueDictEntry(TypedDict, total=True):
    key: str
    value: float
    """number instead of integer because not all uint32 can be represented by int"""
    filteringId: UnsignedInt64AsBase10
class AttributionReportingAggregatableValueEntry(TypedDict, total=True):
    values: List[AttributionReportingAggregatableValueDictEntry]
    filters: AttributionReportingFilterPair
class AttributionReportingEventTriggerData(TypedDict, total=True):
    data: UnsignedInt64AsBase10
    priority: SignedInt64AsBase10
    filters: AttributionReportingFilterPair
    dedupKey: NotRequired[UnsignedInt64AsBase10]
class AttributionReportingAggregatableTriggerData(TypedDict, total=True):
    keyPiece: UnsignedInt128AsBase16
    sourceKeys: List[str]
    filters: AttributionReportingFilterPair
class AttributionReportingAggregatableDedupKey(TypedDict, total=True):
    filters: AttributionReportingFilterPair
    dedupKey: NotRequired[UnsignedInt64AsBase10]
class AttributionReportingNamedBudgetCandidate(TypedDict, total=True):
    filters: AttributionReportingFilterPair
    name: NotRequired[str]
class AttributionReportingTriggerRegistration(TypedDict, total=True):
    filters: AttributionReportingFilterPair
    aggregatableDedupKeys: List[AttributionReportingAggregatableDedupKey]
    eventTriggerData: List[AttributionReportingEventTriggerData]
    aggregatableTriggerData: List[AttributionReportingAggregatableTriggerData]
    aggregatableValues: List[AttributionReportingAggregatableValueEntry]
    aggregatableFilteringIdMaxBytes: int
    debugReporting: bool
    sourceRegistrationTimeConfig: AttributionReportingSourceRegistrationTimeConfig
    aggregatableDebugReportingConfig: AttributionReportingAggregatableDebugReportingConfig
    scopes: List[str]
    namedBudgets: List[AttributionReportingNamedBudgetCandidate]
    debugKey: NotRequired[UnsignedInt64AsBase10]
    aggregationCoordinatorOrigin: NotRequired[str]
    triggerContextId: NotRequired[str]
AttributionReportingEventLevelResult = Literal['success','successDroppedLowerPriority','internalError','noCapacityForAttributionDestination','noMatchingSources','deduplicated','excessiveAttributions','priorityTooLow','neverAttributedSource','excessiveReportingOrigins','noMatchingSourceFilterData','prohibitedByBrowserPolicy','noMatchingConfigurations','excessiveReports','falselyAttributedSource','reportWindowPassed','notRegistered','reportWindowNotStarted','noMatchingTriggerData']
AttributionReportingAggregatableResult = Literal['success','internalError','noCapacityForAttributionDestination','noMatchingSources','excessiveAttributions','excessiveReportingOrigins','noHistograms','insufficientBudget','insufficientNamedBudget','noMatchingSourceFilterData','notRegistered','prohibitedByBrowserPolicy','deduplicated','reportWindowPassed','excessiveReports']
AttributionReportingReportResult = Literal['sent','prohibited','failedToAssemble','expired']
class RelatedWebsiteSet(TypedDict, total=True):
    """A single Related Website Set object."""
    primarySites: List[str]
    """The primary site of this set, along with the ccTLDs if there is any."""
    associatedSites: List[str]
    """The associated sites of this set, along with the ccTLDs if there is any."""
    serviceSites: List[str]
    """The service sites of this set, along with the ccTLDs if there is any."""