from pydantic import BaseModel
from typing import List, Optional

class OrderTypeDto(BaseModel):
    name: Optional[str] = None