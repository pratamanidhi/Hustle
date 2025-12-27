from pydantic import BaseModel
from typing import List, Optional

class PipDto(BaseModel):
    name: Optional[str] = None
    ingredient: Optional[str] = None
    price: Optional[float] = None
    inputedBy: Optional[str] = None