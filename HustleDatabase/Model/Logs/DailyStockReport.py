from pydantic import BaseModel
class DailyStockReport(BaseModel):
    guid: str = None
    name: str = None
    stockOut: int = None
    stockIn: int = None
    totalStockTransaction: int = None
    category: str = None
    datetime: str = None
    lastUpdated: str = None
