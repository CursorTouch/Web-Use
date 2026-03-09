from src.messages import SystemMessage, HumanMessage, ImageMessage
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING
import platform

if TYPE_CHECKING:
    from src.agent.session import Session

_template_cache: dict[str, str] = {}

def _load_template(filename: str) -> str:
    if filename not in _template_cache:
        _template_cache[filename] = Path(f'./src/agent/context/prompt/{filename}').read_text(encoding='utf-8')
    return _template_cache[filename]


class Context:
    """Builds prompt messages (system, state, task) for the agent loop."""

    def __init__(self, session: 'Session'):
        self.session = session

    def system(self, instructions: list[str] = [], max_steps: int = 25) -> SystemMessage:
        browser = self.session.browser
        template = _load_template('system.md')
        content = template.format(**{
            'datetime':      datetime.now().strftime('%A, %B %d, %Y'),
            'os':            platform.system(),
            'browser':       browser.config.browser.capitalize(),
            'home_dir':      Path.home().as_posix(),
            'downloads_dir': browser.config.downloads_dir,
            'max_steps':     max_steps,
            'instructions':  '\n'.join(f'{i+1}. {ins}' for i, ins in enumerate(instructions)) if instructions else '',
        })
        return SystemMessage(content=content)

    async def state(self, query: str, step: int, max_steps: int,
                    tool_result: str = 'No previous action.',
                    use_vision: bool = False) -> HumanMessage | ImageMessage:
        browser_state = await self.session.get_state(use_vision=use_vision)
        template = _load_template('state.md')
        content = template.format(**{
            'step':                 step,
            'max_steps':            max_steps,
            'current_tab':          browser_state.current_tab.to_string() if browser_state.current_tab else 'None',
            'tabs':                 browser_state.tabs_to_string(),
            'interactive_elements': browser_state.dom_state.interactive_elements_to_string(),
            'scrollable_elements':  browser_state.dom_state.scrollable_elements_to_string(),
            'informative_elements': browser_state.dom_state.informative_elements_to_string(),
            'tool_result':          tool_result,
            'query':                query,
        })
        if use_vision and browser_state.screenshot:
            from PIL import Image
            import io
            img = Image.open(io.BytesIO(browser_state.screenshot))
            return ImageMessage(content=content, images=[img])
        return HumanMessage(content=content)

    def task(self, task: str) -> HumanMessage:
        return HumanMessage(content=f'TASK: {task}')
