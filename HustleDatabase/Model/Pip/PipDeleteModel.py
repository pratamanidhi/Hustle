from pydantic import BaseModel
from typing import Optional

class PipDeleteModel(BaseModel):
    name: str