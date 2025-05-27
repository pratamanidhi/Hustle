from dataclasses import dataclass
from datetime import datetime

@dataclass
class ToppingModel:
    guid: str
    name: str
    description: str
    stockInt: int
    stockOut: int
    totalStock: int
    lastInput: datetime
    lastOutput: datetime
    updatedBy: str
    price: int