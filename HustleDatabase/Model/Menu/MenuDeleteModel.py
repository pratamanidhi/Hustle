from pydantic import BaseModel
from typing import Optional

class MenuDeleteModel(BaseModel):
    name: str