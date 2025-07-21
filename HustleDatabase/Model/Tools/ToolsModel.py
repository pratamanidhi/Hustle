from pydantic import BaseModel
class ToolsModel(BaseModel):
    guid: str = None
    name: str = None
    updatedAt: str = None