from src.agent.browser.config import BrowserConfig
from src.providers.nvidia import ChatNvidia
from src.agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

# browser_instance_dir = os.getenv('BROWSER_INSTANCE_DIR')
# user_data_dir = os.getenv('USER_DATA_DIR')

llm=ChatNvidia(model='qwen/qwen3.5-122b-a10b',temperature=0)
config=BrowserConfig(browser='edge',headless=False)

agent=Agent(config=config,llm=llm,use_vision=True,max_steps=100)
user_query = input('Enter your query: ')
agent.print_response(user_query)