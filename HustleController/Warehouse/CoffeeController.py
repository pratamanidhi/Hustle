from fastapi import APIRouter
from HustleBussiness.Warehouse.CoffeeBussiness import CoffeeBusiness as Coffee
from HustleDatabase.Model.Warehouse.CoffeeModel import CoffeeModel as Model

router = APIRouter()
service = Coffee()

@router.get("/get-stock-coffee")
def GetStock():
    return service.GetStock()

@router.put("/update-stock")
def UpdateStock(isOut: bool, coffee: Model):
    return service.UpdateStock(isOut, coffee)

