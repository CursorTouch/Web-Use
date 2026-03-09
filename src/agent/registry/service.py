from src.agent.registry.views import ToolResult
from src.tools import Tool


class Registry:
    def __init__(self, tools: list[Tool] = []):
        self.tools = tools
        self.tools_registry = {tool.name: tool for tool in tools}

    def get_tools(self, exclude: list[str] = []) -> list[Tool]:
        if not exclude:
            return self.tools
        return [t for t in self.tools if t.name not in exclude]

    def get_tool(self, name: str) -> Tool | None:
        return self.tools_registry.get(name)

    def execute(self, tool_name: str, tool_params: dict, session=None) -> ToolResult:
        tool = self.get_tool(tool_name)
        if not tool:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' not found.")
        errors = tool.validate_params(tool_params)
        if errors:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' validation failed:\n" + "\n".join(errors))
        try:
            content = tool.invoke(**({'session': session} | tool_params))
            return ToolResult(is_success=True, content=content)
        except Exception as e:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' failed: {e}")

    async def aexecute(self, tool_name: str, tool_params: dict, session=None) -> ToolResult:
        tool = self.get_tool(tool_name)
        if not tool:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' not found.")
        errors = tool.validate_params(tool_params)
        if errors:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' validation failed:\n" + "\n".join(errors))
        try:
            content = await tool.ainvoke(**({'session': session} | tool_params))
            return ToolResult(is_success=True, content=content)
        except Exception as e:
            return ToolResult(is_success=False, error=f"Tool '{tool_name}' async failed: {e}")
