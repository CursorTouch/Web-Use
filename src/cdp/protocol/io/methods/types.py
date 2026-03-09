"""CDP IO Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.io.types import StreamHandle
    from cdp.protocol.runtime.types import RemoteObjectId

class closeParameters(TypedDict, total=True):
    handle: StreamHandle
    """Handle of the stream to close."""
class readParameters(TypedDict, total=True):
    handle: StreamHandle
    """Handle of the stream to read."""
    offset: NotRequired[int]
    """Seek to the specified offset before reading (if not specified, proceed with offset following the last read). Some types of streams may only support sequential reads."""
    size: NotRequired[int]
    """Maximum number of bytes to read (left upon the agent discretion if not specified)."""
class resolveBlobParameters(TypedDict, total=True):
    objectId: RemoteObjectId
    """Object id of a Blob object wrapper."""

class readReturns(TypedDict):
    base64Encoded: bool
    """Set if the data is base64-encoded"""
    data: str
    """Data that were read."""
    eof: bool
    """Set if the end-of-file condition occurred while reading."""
class resolveBlobReturns(TypedDict):
    uuid: str
    """UUID of the specified Blob."""