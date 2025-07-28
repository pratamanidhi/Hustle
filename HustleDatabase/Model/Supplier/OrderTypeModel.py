from pydantic import BaseModel

class OrderTypeModel(BaseModel):
    guid: str = None
    name: str = None
    updatedAt: str = None