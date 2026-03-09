from pydantic import BaseModel


class ToolResult(BaseModel):
    is_success: bool = False
    content: str | None = None
    error: str | None = None
