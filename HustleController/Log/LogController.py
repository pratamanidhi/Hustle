from fastapi import APIRouter, Body
from HustleBussiness.Log.LogBusiness import LogBusiness as Log
from HustleDatabase.Model.Logs.LogModel import LogModel as Model
from HustleDatabase.Model.Logs.DailyStockReport import DailyStockReport as StockModel

router = APIRouter()
service = Log()

@router.get("/get-log")
def GetLogs():
    return service.GetLogs()

@router.post("/insert-log")
def InsertLog(model: Model = Body(...)):
    return service.InsertLog(model)

@router.post("/insert-daily-log")
def InsertDaily(model: StockModel = Body(...)):
    return service.InputIntoDailyStockReport(model)