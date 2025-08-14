from pydantic import BaseModel

class SupplierByCategoryDto(BaseModel):
    name: str