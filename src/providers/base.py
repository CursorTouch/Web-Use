from typing import Protocol, runtime_checkable, overload, Iterator, AsyncIterator
from src.providers.events import LLMEvent, LLMStreamEvent
from src.providers.views import Metadata
from src.messages import BaseMessage
from collections.abc import Iterable
from src.tools import Tool
from pydantic import BaseModel


@runtime_checkable
class BaseChatLLM(Protocol):

    def sanitize_schema(self, tool_schema: dict) -> dict:
        params = tool_schema.get("parameters", {})
        properties = params.get("properties", {})
        required = params.get("required", [])

        clean_props = {}
        for name, prop in properties.items():
            if isinstance(prop, dict):
                t = prop.get("type", "string")
                enum_vals = prop.get("enum")
                description = prop.get("description")
            else:
                t = "string"
                enum_vals = None
                description = None

            if t not in {"string", "integer", "number", "boolean", "array", "object"}:
                t = "string"

            entry: dict = {"type": t}
            if enum_vals is not None:
                entry["enum"] = enum_vals
            if description is not None:
                entry["description"] = description
            clean_props[name] = entry

        return {
            "name": tool_schema.get("name"),
            "description": tool_schema.get("description"),
            "parameters": {
                "type": "object",
                "properties": clean_props,
                "required": required,
            },
        }

    @property
    def model_name(self) -> str: ...

    @property
    def provider(self) -> str: ...

    @overload
    def invoke(self, messages: list[BaseMessage] | Iterable[BaseMessage], tools: list[Tool] = [], structured_output: BaseModel | None = None, json_mode: bool = False) -> LLMEvent: ...

    @overload
    async def ainvoke(self, messages: list[BaseMessage] | Iterable[BaseMessage], tools: list[Tool] = [], structured_output: BaseModel | None = None, json_mode: bool = False) -> LLMEvent: ...

    @overload
    def stream(self, messages: list[BaseMessage] | Iterable[BaseMessage], tools: list[Tool] = [], structured_output: BaseModel | None = None, json_mode: bool = False) -> Iterator[LLMStreamEvent]: ...

    @overload
    async def astream(self, messages: list[BaseMessage] | Iterable[BaseMessage], tools: list[Tool] = [], structured_output: BaseModel | None = None, json_mode: bool = False) -> AsyncIterator[LLMStreamEvent]: ...

    @overload
    def get_metadata(self) -> Metadata: ...
