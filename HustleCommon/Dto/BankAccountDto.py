from pydantic import BaseModel
from typing import List, Optional

class BankAccountDto(BaseModel):
    name: Optional[str] = None
    bankNumber: Optional[int] = None