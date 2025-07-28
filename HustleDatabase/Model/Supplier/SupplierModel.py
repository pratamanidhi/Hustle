from pydantic import BaseModel

class SupplierModel(BaseModel):
    guid: str = None
    name: str = None
    orderType: str = None
    bankNumber: int = None
    bankName: str = None
    contactPerson: str = None
    updatedAt: str = None