"""CDP CacheStorage Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.cache_storage.types import Cache
    from cdp.protocol.cache_storage.types import CacheId
    from cdp.protocol.cache_storage.types import CachedResponse
    from cdp.protocol.cache_storage.types import DataEntry
    from cdp.protocol.cache_storage.types import Header
    from cdp.protocol.storage.types import StorageBucket

class deleteCacheParameters(TypedDict, total=True):
    cacheId: CacheId
    """Id of cache for deletion."""
class deleteEntryParameters(TypedDict, total=True):
    cacheId: CacheId
    """Id of cache where the entry will be deleted."""
    request: str
    """URL spec of the request."""
class requestCacheNamesParameters(TypedDict, total=False):
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""
class requestCachedResponseParameters(TypedDict, total=True):
    cacheId: CacheId
    """Id of cache that contains the entry."""
    requestURL: str
    """URL spec of the request."""
    requestHeaders: List[Header]
    """headers of the request."""
class requestEntriesParameters(TypedDict, total=True):
    cacheId: CacheId
    """ID of cache to get entries from."""
    skipCount: NotRequired[int]
    """Number of records to skip."""
    pageSize: NotRequired[int]
    """Number of records to fetch."""
    pathFilter: NotRequired[str]
    """If present, only return the entries containing this substring in the path"""


class requestCacheNamesReturns(TypedDict):
    caches: List[Cache]
    """Caches for the security origin."""
class requestCachedResponseReturns(TypedDict):
    response: CachedResponse
    """Response read from the cache."""
class requestEntriesReturns(TypedDict):
    cacheDataEntries: List[DataEntry]
    """Array of object store data entries."""
    returnCount: float
    """Count of returned entries from this storage. If pathFilter is empty, it is the count of all entries from this storage."""