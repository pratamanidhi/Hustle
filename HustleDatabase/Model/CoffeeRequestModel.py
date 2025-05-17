from pydantic import BaseModel

class CoffeeRequest(BaseModel):
    name: str
    price: float
