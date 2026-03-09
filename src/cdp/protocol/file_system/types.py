"""CDP FileSystem Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.storage.types import SerializedStorageKey

class File(TypedDict, total=True):
    name: str
    lastModified: TimeSinceEpoch
    """Timestamp"""
    size: float
    """Size in bytes"""
    type: str
class Directory(TypedDict, total=True):
    name: str
    nestedDirectories: List[str]
    nestedFiles: List[File]
    """Files that are directly nested under this directory."""
class BucketFileSystemLocator(TypedDict, total=True):
    storageKey: SerializedStorageKey
    """Storage key"""
    pathComponents: List[str]
    """Path to the directory using each path component as an array item."""
    bucketName: NotRequired[str]
    """Bucket name. Not passing a bucketName will retrieve the default Bucket. (https://developer.mozilla.org/en-US/docs/Web/API/Storage_API#storage_buckets)"""