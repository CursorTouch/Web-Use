from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def invoke(self, task: str):
        pass

    @abstractmethod
    async def ainvoke(self, task: str):
        pass
