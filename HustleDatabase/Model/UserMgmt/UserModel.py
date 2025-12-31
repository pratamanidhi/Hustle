from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    guid: Optional[str] = None