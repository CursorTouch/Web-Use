"""CDP DOMStorage Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom_storage.types import StorageId

class domStorageItemAddedEvent(TypedDict, total=True):
    storageId: StorageId
    key: str
    newValue: str
class domStorageItemRemovedEvent(TypedDict, total=True):
    storageId: StorageId
    key: str
class domStorageItemUpdatedEvent(TypedDict, total=True):
    storageId: StorageId
    key: str
    oldValue: str
    newValue: str
class domStorageItemsClearedEvent(TypedDict, total=True):
    storageId: StorageId