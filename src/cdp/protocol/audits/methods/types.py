"""CDP Audits Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.audits.types import GenericIssueDetails
    from cdp.protocol.network.types import RequestId

class getEncodedResponseParameters(TypedDict, total=True):
    requestId: RequestId
    """Identifier of the network request to get content for."""
    encoding: Literal["webp", "jpeg", "png"]
    """The encoding to use."""
    quality: NotRequired[float]
    """The quality of the encoding (0-1). (defaults to 1)"""
    sizeOnly: NotRequired[bool]
    """Whether to only return the size information (defaults to false)."""



class getEncodedResponseReturns(TypedDict):
    body: str
    """The encoded body as a base64 string. Omitted if sizeOnly is true. (Encoded as a base64 string when passed over JSON)"""
    originalSize: int
    """Size before re-encoding."""
    encodedSize: int
    """Size after re-encoding."""


class checkFormsIssuesReturns(TypedDict):
    formIssues: List[GenericIssueDetails]