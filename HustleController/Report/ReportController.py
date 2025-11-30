from fastapi import APIRouter
from HustleBussiness.Log.LogBusiness import LogBusiness as Report
from HustleCommon.Enums.Ingredient import Ingredient as stockType


router = APIRouter()
service = Report()

@router.get('/get-report')
def GetReport(types: stockType):
    return service.GetReportByCategory(types)

@router.get('/get-report-all')
def GetAllReport():
    return service.GetAllReport()

@router.get('/get-report-all-by-period')
def GetReportByPeriod(start: str, end: str):
    return service.GetReportByPeriod(start, end)