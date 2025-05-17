from fastapi import APIRouter
from HustleBussiness.MilkBaseMenuBussiness import MilkBaseMenuBussiness as MilkBase

router = APIRouter()
service = MilkBase()

@router.get("/get-milkbase")
def GetAllMilkBase():
    return service.GetAllMilkBaseMenu()