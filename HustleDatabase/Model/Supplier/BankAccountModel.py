from pydantic import BaseModel

class BankAccountModel(BaseModel):
    guid: str = None
    name: str = None
    bankNumber: int = None
    updatedAt: str = None