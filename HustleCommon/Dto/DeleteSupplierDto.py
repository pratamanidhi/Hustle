from pydantic import BaseModel
from typing import Optional

class DeleteSupplierDto(BaseModel):
    guid: Optional[str] = None