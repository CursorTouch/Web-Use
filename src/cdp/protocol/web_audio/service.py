"""CDP WebAudio Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import WebAudioMethods
from .events.service import WebAudioEvents

if TYPE_CHECKING:
    from ...service import Client

class WebAudio(WebAudioMethods, WebAudioEvents):
    """
    This domain allows inspection of Web Audio API. https://webaudio.github.io/web-audio-api/
    """
    def __init__(self, client: Client):
        """
        Initialize the WebAudio domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        WebAudioMethods.__init__(self, client)
        WebAudioEvents.__init__(self, client)