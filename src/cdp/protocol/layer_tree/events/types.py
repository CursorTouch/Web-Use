"""CDP LayerTree Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import Rect
    from cdp.protocol.layer_tree.types import Layer
    from cdp.protocol.layer_tree.types import LayerId

class layerPaintedEvent(TypedDict, total=True):
    layerId: LayerId
    """The id of the painted layer."""
    clip: Rect
    """Clip rectangle."""
class layerTreeDidChangeEvent(TypedDict, total=False):
    layers: NotRequired[List[Layer]]
    """Layer tree, absent if not in the compositing mode."""