from dataclasses import dataclass

@dataclass
class MilkBase:
    guid: str
    name: str
    price: int
    isDeleted: bool