from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class TeaModel:
    guid: str
    name: str = None
    description: str = None
    stockIn: int = None
    stockOut: int = None
    totalStock: int = None
    updatedBy: str = None
    price: int = None
    unit: str = None
    packaging: int = None
    priceUnit: float = None
    lastInput: Optional[datetime] = None
    lastOutput: Optional[datetime] = None