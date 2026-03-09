"""CDP Media Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.media.types import Player
    from cdp.protocol.media.types import PlayerError
    from cdp.protocol.media.types import PlayerEvent
    from cdp.protocol.media.types import PlayerId
    from cdp.protocol.media.types import PlayerMessage
    from cdp.protocol.media.types import PlayerProperty

class playerPropertiesChangedEvent(TypedDict, total=True):
    playerId: PlayerId
    properties: List[PlayerProperty]
class playerEventsAddedEvent(TypedDict, total=True):
    playerId: PlayerId
    events: List[PlayerEvent]
class playerMessagesLoggedEvent(TypedDict, total=True):
    playerId: PlayerId
    messages: List[PlayerMessage]
class playerErrorsRaisedEvent(TypedDict, total=True):
    playerId: PlayerId
    errors: List[PlayerError]
class playerCreatedEvent(TypedDict, total=True):
    player: Player