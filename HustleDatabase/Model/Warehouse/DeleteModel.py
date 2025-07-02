from pydantic import BaseModel
from typing import Optional

class DeleteModel(BaseModel):
    guid: str