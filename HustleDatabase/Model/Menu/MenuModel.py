from pydantic import BaseModel
from typing import Optional


class MenuModel(BaseModel):
    guid: str = None
    name: Optional[str] = None
    ingredient: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    lastUpdate: str = None