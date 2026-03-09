"""CDP LayerTree Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import Rect
    from cdp.protocol.layer_tree.types import LayerId
    from cdp.protocol.layer_tree.types import PaintProfile
    from cdp.protocol.layer_tree.types import PictureTile
    from cdp.protocol.layer_tree.types import SnapshotId

class compositingReasonsParameters(TypedDict, total=True):
    layerId: LayerId
    """The id of the layer for which we want to get the reasons it was composited."""


class loadSnapshotParameters(TypedDict, total=True):
    tiles: List[PictureTile]
    """An array of tiles composing the snapshot."""
class makeSnapshotParameters(TypedDict, total=True):
    layerId: LayerId
    """The id of the layer."""
class profileSnapshotParameters(TypedDict, total=True):
    snapshotId: SnapshotId
    """The id of the layer snapshot."""
    minRepeatCount: NotRequired[int]
    """The maximum number of times to replay the snapshot (1, if not specified)."""
    minDuration: NotRequired[float]
    """The minimum duration (in seconds) to replay the snapshot."""
    clipRect: NotRequired[Rect]
    """The clip rectangle to apply when replaying the snapshot."""
class releaseSnapshotParameters(TypedDict, total=True):
    snapshotId: SnapshotId
    """The id of the layer snapshot."""
class replaySnapshotParameters(TypedDict, total=True):
    snapshotId: SnapshotId
    """The id of the layer snapshot."""
    fromStep: NotRequired[int]
    """The first step to replay from (replay from the very start if not specified)."""
    toStep: NotRequired[int]
    """The last step to replay to (replay till the end if not specified)."""
    scale: NotRequired[float]
    """The scale to apply while replaying (defaults to 1)."""
class snapshotCommandLogParameters(TypedDict, total=True):
    snapshotId: SnapshotId
    """The id of the layer snapshot."""
class compositingReasonsReturns(TypedDict):
    compositingReasons: List[str]
    """A list of strings specifying reasons for the given layer to become composited."""
    compositingReasonIds: List[str]
    """A list of strings specifying reason IDs for the given layer to become composited."""


class loadSnapshotReturns(TypedDict):
    snapshotId: SnapshotId
    """The id of the snapshot."""
class makeSnapshotReturns(TypedDict):
    snapshotId: SnapshotId
    """The id of the layer snapshot."""
class profileSnapshotReturns(TypedDict):
    timings: List[PaintProfile]
    """The array of paint profiles, one per run."""

class replaySnapshotReturns(TypedDict):
    dataURL: str
    """A data: URL for resulting image."""
class snapshotCommandLogReturns(TypedDict):
    commandLog: List[Dict[str, Any]]
    """The array of canvas function calls."""