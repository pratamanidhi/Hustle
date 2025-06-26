from fastapi import APIRouter, Body
from HustleBussiness.Log.LogBusiness import LogBusiness as Log
from HustleDatabase.Model.Logs.LogModel import LogModel as Model

router = APIRouter()
service = Log()

@router.get("/get-log")
def GetLogs():
    return service.GetLogs()

@router.post("/insert-log")
def InsertLog(model: Model = Body(...)):
    return service.InsertLog(model)