from src.agent.tools.views import Click, Type, Wait, Scroll, GoTo, Back, Key, Download, Scrape, Tab, Upload, Menu, Done, Forward, HumanInput, Script
from src.agent.session import Session
from markdownify import markdownify
from typing import Literal, Optional
from termcolor import colored
from src.tools import Tool
from asyncio import sleep
from pathlib import Path
from os import getcwd
import httpx


@Tool('Done Tool', model=Done)
async def done_tool(content: str, session: Session = None):
    '''Indicates that the current task has been completed successfully. Use this to signal completion and provide a summary of what was accomplished.'''
    return content


@Tool('Click Tool', model=Click)
async def click_tool(index: int, session: Session = None):
    '''Clicks on interactive elements like buttons, links, checkboxes, radio buttons, tabs, or any clickable UI component. Automatically scrolls the element into view if needed.'''
    element = await session.get_element_by_index(index=index)
    xpath   = element.xpath.get('element', '')
    if xpath:
        await session.scroll_into_view(xpath)
    await session.click_at(element.center.x, element.center.y)
    await session._wait_for_page(timeout=8.0)
    return f'Clicked on the element at label {index}'


@Tool('Type Tool', model=Type)
async def type_tool(index: int, text: str, clear: Literal['True', 'False'] = 'False',
                    press_enter: Literal['True', 'False'] = 'False', session: Session = None):
    '''Types text into input fields, text areas, search boxes, or any editable element. Can optionally clear existing content before typing.'''
    element = await session.get_element_by_index(index=index)
    xpath   = element.xpath.get('element', '')
    if xpath:
        await session.scroll_into_view(xpath)
    await session.click_at(element.center.x, element.center.y)
    if clear == 'True':
        await session.key_press('Control+a')
        await session.key_press('Backspace')
    await session.type_text(text, delay_ms=50)
    if press_enter == 'True':
        await session.key_press('Enter')
        await session._wait_for_page(timeout=8.0)
    return f'Typed {text} in element at label {index}'


@Tool('Wait Tool', model=Wait)
async def wait_tool(time: int, session: Session = None):
    '''Pauses execution for a specified number of seconds. Use this to wait for page loading, animations to complete, or content to appear after an action.'''
    await sleep(time)
    return f'Waited for {time}s'


@Tool('Scroll Tool', model=Scroll)
async def scroll_tool(direction: Literal['up', 'down'] = 'down', index: int = None,
                      amount: int = 500, session: Session = None):
    '''Scrolls either the webpage or a specific scrollable container. If index is provided, scrolls that element; otherwise scrolls the page.'''
    if index is not None:
        element = await session.get_element_by_index(index=index)
        xpath   = element.xpath.get('element', '')
        await session.scroll_element(xpath, direction, amount)
        return f'Scrolled {direction} inside element at label {index} by {amount}px'

    pos        = await session.get_scroll_position()
    scroll_y   = pos.get('scrollY', 0)
    max_scroll = pos.get('scrollHeight', 0) - pos.get('innerHeight', 0)

    if direction == 'down' and scroll_y >= max_scroll:
        return 'Already at the bottom, cannot scroll further.'
    if direction == 'up' and scroll_y <= 0:
        return 'Already at the top, cannot scroll further.'

    await session.scroll_page(direction, amount)
    return f'Scrolled {direction} by {amount}px'


@Tool('GoTo Tool', model=GoTo)
async def goto_tool(url: str, session: Session = None):
    '''Navigates directly to a specified URL in the current tab. Waits for the page to load before proceeding.'''
    await session.navigate(url)
    return f'Navigated to {url}'


@Tool('Back Tool', model=Back)
async def back_tool(session: Session = None):
    '''Navigates to the previous page in browser history, equivalent to clicking the browser Back button.'''
    await session.go_back()
    return 'Navigated to previous page'


@Tool('Forward Tool', model=Forward)
async def forward_tool(session: Session = None):
    '''Navigates to the next page in browser history, equivalent to clicking the browser Forward button.'''
    await session.go_forward()
    return 'Navigated to next page'


@Tool('Key Tool', model=Key)
async def key_tool(keys: str, times: int = 1, session: Session = None):
    '''Performs keyboard shortcuts and key combinations (e.g. "Control+C", "Enter", "Escape", "PageDown"). Can repeat the key press multiple times.'''
    for _ in range(times):
        await session.key_press(keys)
    return f'Pressed {keys}'


@Tool('Download Tool', model=Download)
async def download_tool(url: str = None, filename: str = None, session: Session = None):
    '''Downloads a file from a URL and saves it to the downloads directory.'''
    folder_path = Path(session.browser.config.downloads_dir)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    path = folder_path / filename
    with open(path, 'wb') as f:
        async for chunk in response.aiter_bytes():
            f.write(chunk)
    return f'Downloaded {filename} from {url} and saved to {path}'


@Tool('Scrape Tool', model=Scrape)
async def scrape_tool(session: Session = None):
    '''Extracts and returns the main content from the current webpage in markdown format.'''
    html    = await session.get_page_content()
    content = markdownify(html)
    return f'Scraped the contents of the webpage:\n{content}'


@Tool('Tab Tool', model=Tab)
async def tab_tool(mode: Literal['open', 'close', 'switch'], tab_index: Optional[int] = None,
                   session: Session = None):
    '''Manages browser tabs: opens new blank tabs, closes the current tab, or switches between existing tabs by index.'''
    if mode == 'open':
        await session.new_tab()
        await session._wait_for_page(timeout=5.0)
        return 'Opened a new blank tab and switched to it.'

    elif mode == 'close':
        if len(session._sessions) <= 1:
            return 'Cannot close the last remaining tab.'
        await session.close_tab()
        return 'Closed current tab and switched to the last remaining tab.'

    elif mode == 'switch':
        tabs = await session.get_all_tabs()
        if tab_index is None or tab_index < 0 or tab_index >= len(tabs):
            raise IndexError(f'Tab index {tab_index} out of range. Available: {len(tabs)}')
        await session.switch_tab(tab_index)
        await session._wait_for_page(timeout=5.0)
        return f'Switched to tab {tab_index} (Total tabs: {len(tabs)}).'

    raise ValueError("Invalid mode. Use 'open', 'close', or 'switch'.")


@Tool('Upload Tool', model=Upload)
async def upload_tool(index: int, filenames: list[str], session: Session = None):
    '''Uploads one or more files to a file input element. Files must be present in the ./uploads directory.'''
    element = await session.get_element_by_index(index=index)
    xpath   = element.xpath.get('element', '')
    files   = [str(Path(getcwd()) / 'uploads' / fn) for fn in filenames]
    await session.set_file_input(xpath, files)
    return f'Uploaded {filenames} to element at label {index}'


@Tool('Menu Tool', model=Menu)
async def menu_tool(index: int, labels: list[str], session: Session = None):
    '''Selects one or more options in a <select> dropdown by their visible label text.'''
    element = await session.get_element_by_index(index=index)
    xpath   = element.xpath.get('element', '')
    await session.select_option(xpath, labels)
    return f'Selected {", ".join(labels)} in element at label {index}'


@Tool('Script Tool', model=Script)
async def script_tool(script: str, session: Session = None):
    '''Executes arbitrary JavaScript on the current page and returns the result.'''
    result = await session.execute_script(script)
    return f'Script result: {result}'


@Tool('Human Tool', model=HumanInput)
async def human_tool(prompt: str, session: Session = None):
    '''Requests human assistance when encountering CAPTCHAs, OTP codes, or other challenges that require a human.'''
    print(colored(f'Agent: {prompt}', color='cyan', attrs=['bold']))
    human_response = input('User: ')
    return f"User provided: '{human_response}'"
