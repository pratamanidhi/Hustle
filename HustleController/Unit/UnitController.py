from fastapi import APIRouter
from HustleBussiness.Unit.UnitBusiness import UnitBusiness as unit

router = APIRouter()
service = unit()

@router.get("/get-unit")
def GetUnit():
    return service.GetUnit()

@router.get("/get-unit-by-name")
def GetUnitByName(param):
    return service.GetUnitByName(param)