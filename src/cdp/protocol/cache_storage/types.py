"""CDP CacheStorage Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.storage.types import StorageBucket

CacheId = str
"""Unique identifier of the Cache object."""
CachedResponseType = Literal['basic','cors','default','error','opaqueResponse','opaqueRedirect']
"""type of HTTP response cached"""
class DataEntry(TypedDict, total=True):
    """Data entry."""
    requestURL: str
    """Request URL."""
    requestMethod: str
    """Request method."""
    requestHeaders: List[Header]
    """Request headers"""
    responseTime: float
    """Number of seconds since epoch."""
    responseStatus: int
    """HTTP response status code."""
    responseStatusText: str
    """HTTP response status text."""
    responseType: CachedResponseType
    """HTTP response type"""
    responseHeaders: List[Header]
    """Response headers"""
class Cache(TypedDict, total=True):
    """Cache identifier."""
    cacheId: CacheId
    """An opaque unique id of the cache."""
    securityOrigin: str
    """Security origin of the cache."""
    storageKey: str
    """Storage key of the cache."""
    cacheName: str
    """The name of the cache."""
    storageBucket: NotRequired[StorageBucket]
    """Storage bucket of the cache."""
class Header(TypedDict, total=True):
    name: str
    value: str
class CachedResponse(TypedDict, total=True):
    """Cached response"""
    body: str
    """Entry content, base64-encoded. (Encoded as a base64 string when passed over JSON)"""