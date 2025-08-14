from pydantic import BaseModel
from typing import List, Optional

class SupplierDto(BaseModel):
    name: Optional[str] = None
    orderType: Optional[str] = None
    productName: Optional[str] = None
    bankNumber: Optional[int] = None
    bankName: Optional[str] = None
    contactPerson: Optional[int] = None