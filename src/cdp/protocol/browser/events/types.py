"""CDP Browser Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.page.types import FrameId

class downloadWillBeginEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that caused the download to begin."""
    guid: str
    """Global unique identifier of the download."""
    url: str
    """URL of the resource being downloaded."""
    suggestedFilename: str
    """Suggested file name of the resource (the actual name of the file saved on disk may differ)."""
class downloadProgressEvent(TypedDict, total=True):
    guid: str
    """Global unique identifier of the download."""
    totalBytes: float
    """Total expected bytes to download."""
    receivedBytes: float
    """Total bytes received."""
    state: Literal["inProgress", "completed", "canceled"]
    """Download status."""
    filePath: NotRequired[str]
    """If download is "completed", provides the path of the downloaded file. Depending on the platform, it is not guaranteed to be set, nor the file is guaranteed to exist."""