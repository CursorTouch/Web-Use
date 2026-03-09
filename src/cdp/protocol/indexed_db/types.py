"""CDP IndexedDB Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.runtime.types import RemoteObject

class DatabaseWithObjectStores(TypedDict, total=True):
    """Database with an array of object stores."""
    name: str
    """Database name."""
    version: float
    """Database version (type is not 'integer', as the standard requires the version number to be 'unsigned long long')"""
    objectStores: List[ObjectStore]
    """Object stores in this database."""
class ObjectStore(TypedDict, total=True):
    """Object store."""
    name: str
    """Object store name."""
    keyPath: KeyPath
    """Object store key path."""
    autoIncrement: bool
    """If true, object store has auto increment flag set."""
    indexes: List[ObjectStoreIndex]
    """Indexes in this object store."""
class ObjectStoreIndex(TypedDict, total=True):
    """Object store index."""
    name: str
    """Index name."""
    keyPath: KeyPath
    """Index key path."""
    unique: bool
    """If true, index is unique."""
    multiEntry: bool
    """If true, index allows multiple entries for a key."""
class Key(TypedDict, total=True):
    """Key."""
    type: Literal["number", "string", "date", "array"]
    """Key type."""
    number: NotRequired[float]
    """Number value."""
    string: NotRequired[str]
    """String value."""
    date: NotRequired[float]
    """Date value."""
    array: NotRequired[List[Key]]
    """Array value."""
class KeyRange(TypedDict, total=True):
    """Key range."""
    lowerOpen: bool
    """If true lower bound is open."""
    upperOpen: bool
    """If true upper bound is open."""
    lower: NotRequired[Key]
    """Lower bound."""
    upper: NotRequired[Key]
    """Upper bound."""
class DataEntry(TypedDict, total=True):
    """Data entry."""
    key: RemoteObject
    """Key object."""
    primaryKey: RemoteObject
    """Primary key object."""
    value: RemoteObject
    """Value object."""
class KeyPath(TypedDict, total=True):
    """Key path."""
    type: Literal["null", "string", "array"]
    """Key path type."""
    string: NotRequired[str]
    """String value."""
    array: NotRequired[List[str]]
    """Array value."""