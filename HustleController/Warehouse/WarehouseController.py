from fastapi import APIRouter, Body
from HustleBussiness.Warehouse.WarehouseBussiness import WarehouseBusiness as wh
from HustleDatabase.Model.Warehouse.WarehouseModel import WarehouseModel as Model
from HustleCommon.Enums.Ingredient import Ingredient as stockType

router = APIRouter()
service = wh()

@router.get("/get-stock")
def GetStock(types: stockType):
    return service.GetStock(types)

@router.post("/add-stock")
def AddStock(types: stockType, model: Model = Body(...)):
    return service.AddStock(types, model)

@router.put("/update-stock")
def UpdateStock(types: stockType, isOut: bool, model: Model = Body(...)):
    return service.UpdateStock(types, isOut, model)

