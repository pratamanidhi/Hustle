from pydantic import BaseModel
from typing import Optional

class PipModel(BaseModel):
    guid: str = None
    name: Optional[str] = None
    ingredient: Optional[str] = None
    price: Optional[float] = None
    lastUpdate: str = None