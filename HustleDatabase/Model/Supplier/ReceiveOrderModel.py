from pydantic import BaseModel

class ReceiveOrderModel(BaseModel):
    guid: str = None
    supplierId: str = None
    quantity: str = None
    updatedAt: str = None