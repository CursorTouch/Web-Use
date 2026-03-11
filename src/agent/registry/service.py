from src.agent.registry.views import ToolResult
from src.tools import Tool
import inspect


class Registry:
    def __init__(self, tools: list[Tool] = []):
        self.tools = tools
        self.tools_registry = {tool.name: tool for tool in tools}
        self.extensions: dict = {}

    def add_extension(self, name: str, obj) -> None:
        self.extensions[name] = obj

    def _build_kwargs(self, tool: Tool, tool_params: dict) -> dict:
        """Merge extensions into tool_params, but only for params the tool accepts."""
        sig = inspect.signature(tool.function)
        accepted = set(sig.parameters)
        extensions = {k: v for k, v in self.extensions.items() if k in accepted}
        return extensions | tool_params

    def get_tools(self, exclude: list[str] = []) -> list[Tool]:
        if not exclude:
            return self.tools
        return [t for t in self.tools if t.name not in exclude]

    def get_tool(self, name: str) -> Tool | None:
        return self.tools_registry.get(name)

    def execute(self, tool_name: str, tool_params: dict) -> ToolResult:
        tool = self.get_tool(tool_name)
        if not tool:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' not found.")
        errors = tool.validate_params(tool_params)
        if errors:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' validation failed:\n" + "\n".join(errors))
        try:
            content = tool.invoke(**self._build_kwargs(tool, tool_params))
            return ToolResult(is_success=True, content=content)
        except Exception as e:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' failed: {e}")

    async def aexecute(self, tool_name: str, tool_params: dict) -> ToolResult:
        tool = self.get_tool(tool_name)
        if not tool:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' not found.")
        errors = tool.validate_params(tool_params)
        if errors:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' validation failed:\n" + "\n".join(errors))
        try:
            content = await tool.ainvoke(**self._build_kwargs(tool, tool_params))
            return ToolResult(is_success=True, content=content)
        except Exception as e:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' async failed: {e}")
