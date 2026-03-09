"""CDP BluetoothEmulation Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import BluetoothEmulationMethods
from .events.service import BluetoothEmulationEvents

if TYPE_CHECKING:
    from ...service import Client

class BluetoothEmulation(BluetoothEmulationMethods, BluetoothEmulationEvents):
    """
    This domain allows configuring virtual Bluetooth devices to test the web-bluetooth API.
    """
    def __init__(self, client: Client):
        """
        Initialize the BluetoothEmulation domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        BluetoothEmulationMethods.__init__(self, client)
        BluetoothEmulationEvents.__init__(self, client)