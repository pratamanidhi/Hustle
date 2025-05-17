from dataclasses import dataclass

@dataclass
class Coffee:
    guid: str
    name: str
    price: int
    isDeleted: bool