from pydantic import BaseModel
from typing import Optional

class WarehouseModel(BaseModel):
    guid: str = None
    name: Optional[str] = None
    description: Optional[str] = None
    stockIn: Optional[int] = None
    stockOut: Optional[int] = None
    totalStock: Optional[int] = None
    updatedBy: Optional[str] = None
    price: Optional[int] = None
    unit: Optional[str] = None
    packaging: Optional[int] = None
    priceUnit: Optional[float] = None
    lastInput: Optional[str] = None
    lastOutput: Optional[str] = None
