from dataclasses import dataclass, field
from src.agent.dom.views import DOMState


@dataclass
class Tab:
    id: int
    url: str
    title: str
    target_id: str
    session_id: str

    def to_string(self) -> str:
        return f'{self.id} - Title: {self.title} - URL: {self.url}'


@dataclass
class BrowserState:
    current_tab: Tab | None = None
    tabs: list[Tab] = field(default_factory=list)
    screenshot: bytes | None = None
    dom_state: DOMState = field(default_factory=DOMState)

    def tabs_to_string(self) -> str:
        return '\n'.join(tab.to_string() for tab in self.tabs)
