"""CDP Fetch Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.fetch.types import AuthChallenge
    from cdp.protocol.fetch.types import HeaderEntry
    from cdp.protocol.fetch.types import RequestId
    from cdp.protocol.network.types import ErrorReason
    from cdp.protocol.network.types import Request
    from cdp.protocol.network.types import RequestId
    from cdp.protocol.network.types import ResourceType
    from cdp.protocol.page.types import FrameId

class requestPausedEvent(TypedDict, total=True):
    requestId: RequestId
    """Each request the page makes will have a unique id."""
    request: Request
    """The details of the request."""
    frameId: FrameId
    """The id of the frame that initiated the request."""
    resourceType: ResourceType
    """How the requested resource will be used."""
    responseErrorReason: NotRequired[ErrorReason]
    """Response error if intercepted at response stage."""
    responseStatusCode: NotRequired[int]
    """Response code if intercepted at response stage."""
    responseStatusText: NotRequired[str]
    """Response status text if intercepted at response stage."""
    responseHeaders: NotRequired[List[HeaderEntry]]
    """Response headers if intercepted at the response stage."""
    networkId: NotRequired[RequestId]
    """If the intercepted request had a corresponding Network.requestWillBeSent event fired for it, then this networkId will be the same as the requestId present in the requestWillBeSent event."""
    redirectedRequestId: NotRequired[RequestId]
    """If the request is due to a redirect response from the server, the id of the request that has caused the redirect."""
class authRequiredEvent(TypedDict, total=True):
    requestId: RequestId
    """Each request the page makes will have a unique id."""
    request: Request
    """The details of the request."""
    frameId: FrameId
    """The id of the frame that initiated the request."""
    resourceType: ResourceType
    """How the requested resource will be used."""
    authChallenge: AuthChallenge
    """Details of the Authorization Challenge encountered. If this is set, client should respond with continueRequest that contains AuthChallengeResponse."""