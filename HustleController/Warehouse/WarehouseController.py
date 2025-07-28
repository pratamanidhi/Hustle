from fastapi import APIRouter, Body
from HustleBussiness.Warehouse.WarehouseBussiness import WarehouseBusiness as wh
from HustleDatabase.Model.Warehouse.WarehouseModel import WarehouseModel as Model
from HustleDatabase.Model.Warehouse.DeleteModel import DeleteModel as DelModel
from HustleDatabase.Model.Logs.DailyLogModel import DailyLogModel as DailyModel
from HustleCommon.Enums.Ingredient import Ingredient as stockType
from HustleBussiness.Tools.ToolsBusiness import ToolsBusiness as Tools
from HustleCommon.Dto.ToolsDto import ToolsDto

router = APIRouter()
service = wh()
toolsService = Tools()

@router.get("/get-stock")
def GetStock(types: stockType):
    return service.GetStock(types)

@router.post("/add-stock")
def AddStock(types: stockType, model: Model = Body(...)):
    return service.AddStock(types, model)

@router.put("/update-stock")
def UpdateStock(types: stockType, isOut: bool, model: Model = Body(...)):
    return service.UpdateStock(types, isOut, model)

@router.post("/add-daily-log")
def AddDailyLog(model: DailyModel = Body(...)):
    return service.InsertIntoDaliyLog(model)

@router.delete("/delete")
def DeleteStock(types: stockType, model: DelModel = Body(...)):
    return service.DeleteStock(types, model)

@router.get("/get-all-stock")
def GetAllStock():
    return service.GetAllStock()

@router.get('/get-tools')
def GetTools():
    return toolsService.GetAllTools()

@router.post('/input-tools')
def InputTools(model: ToolsDto = Body(...)):
    return toolsService.InputTools(model)