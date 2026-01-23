from pydantic import BaseModel
from typing import Optional

class UpdateUserModel(BaseModel):
    userId: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    isAdmin: Optional[bool] = None