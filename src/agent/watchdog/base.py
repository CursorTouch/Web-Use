from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.agent.session import Session


class BaseWatchdog(ABC):
    def __init__(self, session: 'Session'):
        self.session = session

    @abstractmethod
    async def attach(self) -> None:
        """Register CDP event listeners. Called during session init."""
        ...

    async def detach(self) -> None:
        """Clean up. Called during session close."""
        pass
