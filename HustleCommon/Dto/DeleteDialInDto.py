from pydantic import BaseModel
from typing import Optional

class DeleteDialInDto(BaseModel):
    guid: Optional[str] = None