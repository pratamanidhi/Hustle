from pydantic import BaseModel
class DailyLogModel(BaseModel):
    guid: str = None
    name: str = None
    stockIn: int = None
    stockOut: int = None
    price: int = None
    timestamp: str = None