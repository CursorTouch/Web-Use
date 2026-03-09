"""CDP IndexedDB Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.indexed_db.types import DataEntry
    from cdp.protocol.indexed_db.types import DatabaseWithObjectStores
    from cdp.protocol.indexed_db.types import KeyRange
    from cdp.protocol.storage.types import StorageBucket

class clearObjectStoreParameters(TypedDict, total=True):
    databaseName: str
    """Database name."""
    objectStoreName: str
    """Object store name."""
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""
class deleteDatabaseParameters(TypedDict, total=True):
    databaseName: str
    """Database name."""
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""
class deleteObjectStoreEntriesParameters(TypedDict, total=True):
    databaseName: str
    objectStoreName: str
    keyRange: KeyRange
    """Range of entry keys to delete"""
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""


class requestDataParameters(TypedDict, total=True):
    databaseName: str
    """Database name."""
    objectStoreName: str
    """Object store name."""
    skipCount: int
    """Number of records to skip."""
    pageSize: int
    """Number of records to fetch."""
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""
    indexName: NotRequired[str]
    """Index name. If not specified, it performs an object store data request."""
    keyRange: NotRequired[KeyRange]
    """Key range."""
class getMetadataParameters(TypedDict, total=True):
    databaseName: str
    """Database name."""
    objectStoreName: str
    """Object store name."""
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""
class requestDatabaseParameters(TypedDict, total=True):
    databaseName: str
    """Database name."""
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""
class requestDatabaseNamesParameters(TypedDict, total=False):
    securityOrigin: NotRequired[str]
    """At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin."""
    storageKey: NotRequired[str]
    """Storage key."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket. If not specified, it uses the default bucket."""





class requestDataReturns(TypedDict):
    objectStoreDataEntries: List[DataEntry]
    """Array of object store data entries."""
    hasMore: bool
    """If true, there are more entries to fetch in the given range."""
class getMetadataReturns(TypedDict):
    entriesCount: float
    """the entries count"""
    keyGeneratorValue: float
    """the current value of key generator, to become the next inserted key into the object store. Valid if objectStore.autoIncrement is true."""
class requestDatabaseReturns(TypedDict):
    databaseWithObjectStores: DatabaseWithObjectStores
    """Database with an array of object stores."""
class requestDatabaseNamesReturns(TypedDict):
    databaseNames: List[str]
    """Database names for origin."""