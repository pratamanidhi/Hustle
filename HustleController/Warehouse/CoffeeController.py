from fastapi import APIRouter
from HustleBussiness.Warehouse.CoffeeBussiness import CoffeeBusiness as Coffee

router = APIRouter()
service = Coffee()

@router.get("/get-stock-coffee")
def GetStock():
    return service.GetStock()