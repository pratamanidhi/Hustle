from pydantic import BaseModel
from typing import Optional

class LogModel(BaseModel):
    guid: str = None
    user: str = None
    action: str = None
    timestamp: str = None
