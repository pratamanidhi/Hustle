from pydantic import BaseModel
from typing import Optional

class ReceiveOrderDto(BaseModel):
    supplierId: Optional[str] = None
    quantity: Optional[int] = None
    receiveBy: Optional[str] = None