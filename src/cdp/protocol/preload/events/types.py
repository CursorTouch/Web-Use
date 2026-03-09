"""CDP Preload Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import LoaderId
    from cdp.protocol.network.types import RequestId
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.preload.types import PrefetchStatus
    from cdp.protocol.preload.types import PreloadPipelineId
    from cdp.protocol.preload.types import PreloadingAttemptKey
    from cdp.protocol.preload.types import PreloadingAttemptSource
    from cdp.protocol.preload.types import PreloadingStatus
    from cdp.protocol.preload.types import PrerenderFinalStatus
    from cdp.protocol.preload.types import PrerenderMismatchedHeaders
    from cdp.protocol.preload.types import RuleSet
    from cdp.protocol.preload.types import RuleSetId

class ruleSetUpdatedEvent(TypedDict, total=True):
    ruleSet: RuleSet
class ruleSetRemovedEvent(TypedDict, total=True):
    id: RuleSetId
class preloadEnabledStateUpdatedEvent(TypedDict, total=True):
    disabledByPreference: bool
    disabledByDataSaver: bool
    disabledByBatterySaver: bool
    disabledByHoldbackPrefetchSpeculationRules: bool
    disabledByHoldbackPrerenderSpeculationRules: bool
class prefetchStatusUpdatedEvent(TypedDict, total=True):
    key: PreloadingAttemptKey
    pipelineId: PreloadPipelineId
    initiatingFrameId: FrameId
    """The frame id of the frame initiating prefetch."""
    prefetchUrl: str
    status: PreloadingStatus
    prefetchStatus: PrefetchStatus
    requestId: RequestId
class prerenderStatusUpdatedEvent(TypedDict, total=True):
    key: PreloadingAttemptKey
    pipelineId: PreloadPipelineId
    status: PreloadingStatus
    prerenderStatus: NotRequired[PrerenderFinalStatus]
    disallowedMojoInterface: NotRequired[str]
    """This is used to give users more information about the name of Mojo interface that is incompatible with prerender and has caused the cancellation of the attempt."""
    mismatchedHeaders: NotRequired[List[PrerenderMismatchedHeaders]]
class preloadingAttemptSourcesUpdatedEvent(TypedDict, total=True):
    loaderId: LoaderId
    preloadingAttemptSources: List[PreloadingAttemptSource]