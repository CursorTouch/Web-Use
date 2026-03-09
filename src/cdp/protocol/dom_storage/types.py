"""CDP DOMStorage Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

SerializedStorageKey = str
class StorageId(TypedDict, total=True):
    """DOM Storage identifier."""
    isLocalStorage: bool
    """Whether the storage is local storage (not session storage)."""
    securityOrigin: NotRequired[str]
    """Security origin for the storage."""
    storageKey: NotRequired[SerializedStorageKey]
    """Represents a key by which DOM Storage keys its CachedStorageAreas"""
Item = List[str]
"""DOM Storage item."""