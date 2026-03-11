from src.agent.browser.config import BrowserConfig
from src.providers.nvidia import ChatNvidia
from src.agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatNvidia(model='qwen/qwen3.5-122b-a10b', temperature=0)
config = BrowserConfig(browser='chrome', headless=False)
agent = Agent(config=config, llm=llm, use_vision=True, max_steps=100)

user_query = input('Enter your query: ')
agent.print_response(user_query)