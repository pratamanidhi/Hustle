from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class CoffeeModel:
    guid: str
    name: str
    description: str
    stockIn: int
    stockOut: int
    totalStock: int
    updatedBy: str
    price: int
    unit: str
    packaging: int
    priceUnit: float
    lastInput: Optional[datetime] = None
    lastOutput: Optional[datetime] = None
