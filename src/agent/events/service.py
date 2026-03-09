from __future__ import annotations
from typing import Callable, Union
from src.agent.events.views import AgentEvent
from src.agent.events.subscriber import BaseEventSubscriber

EventSubscriber = Union[BaseEventSubscriber, Callable[[AgentEvent], None]]


class Event:
    def __init__(self) -> None:
        self._subscribers: list[EventSubscriber] = []

    def add_subscriber(self, subscriber: EventSubscriber) -> None:
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: EventSubscriber) -> None:
        self._subscribers.remove(subscriber)

    def emit(self, event: AgentEvent) -> None:
        for subscriber in self._subscribers:
            try:
                if isinstance(subscriber, BaseEventSubscriber):
                    subscriber.invoke(event)
                else:
                    subscriber(event)
            except Exception:
                pass

    def close(self) -> None:
        for subscriber in self._subscribers:
            if isinstance(subscriber, BaseEventSubscriber):
                try:
                    subscriber.close()
                except Exception:
                    pass
        self._subscribers.clear()
