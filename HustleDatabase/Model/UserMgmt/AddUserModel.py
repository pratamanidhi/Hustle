from pydantic import BaseModel
from typing import Optional

class AddUserModel(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    isAdmin: Optional[bool] = None