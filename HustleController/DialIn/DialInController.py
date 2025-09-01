from fastapi import APIRouter, Body
from HustleBussiness.DialIn.DialInBusiness import DialInBusiness as Business
from HustleCommon.Dto.DialInDto import DialInDto as DialInDto
from HustleCommon.Dto.DeleteDialInDto import DeleteDialInDto as DeleteDialInDto

router = APIRouter()
service = Business()

@router.get('/get-all-dialIn')
def GetAllDialIn():
    return service.GetAllDialIn()

@router.post('/add-dialIn')
def InsertDialIn(model: DialInDto = Body(...)):
    return service.InputDialIn(model)

@router.delete('/delete-dialIn')
def DeleteDialIn(model: DeleteDialInDto = Body(...)):
    return service.DeleteDialIn(model)