from pydantic import BaseModel

class SupplierModel(BaseModel):
    guid: str = None
    name: str = None
    orderType: str = None,
    productName: str = None,
    bankAccount: str = None
    contactPerson: str = None
    updatedAt: str = None