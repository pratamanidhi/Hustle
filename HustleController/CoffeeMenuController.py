from fastapi import APIRouter
from HustleBussiness.CoffeeMenuBussiness import CoffeeMenuBussiness as Coffee
from HustleDatabase.Model.CoffeeRequestModel import CoffeeRequest as CreateCoffee

router = APIRouter()
service = Coffee()

@router.get("/get-coffee")
def GetAllCoffee():
    return service.GetAllCoffeeMenus()

@router.post("/add-coffee")
def CreateMenuCoffee(coffee : CreateCoffee):
    return service.CreateCoffeeMenu(coffee)