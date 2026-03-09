"""CDP Extensions Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.extensions.types import ExtensionInfo
    from cdp.protocol.extensions.types import StorageArea

class triggerActionParameters(TypedDict, total=True):
    id: str
    """Extension id."""
    targetId: str
    """A tab target ID to trigger the default extension action on."""
class loadUnpackedParameters(TypedDict, total=True):
    path: str
    """Absolute file path."""
    enableInIncognito: NotRequired[bool]
    """Enable the extension in incognito"""

class uninstallParameters(TypedDict, total=True):
    id: str
    """Extension id."""
class getStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to retrieve data from."""
    keys: NotRequired[List[str]]
    """Keys to retrieve."""
class removeStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to remove data from."""
    keys: List[str]
    """Keys to remove."""
class clearStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to remove data from."""
class setStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to set data in."""
    values: Dict[str, Any]
    """Values to set."""

class loadUnpackedReturns(TypedDict):
    id: str
    """Extension id."""
class getExtensionsReturns(TypedDict):
    extensions: List[ExtensionInfo]

class getStorageItemsReturns(TypedDict):
    data: Dict[str, Any]