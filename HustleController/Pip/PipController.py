from fastapi import APIRouter, Body
from HustleBussiness.Pip.PipBussiness import PipBussiness as Bussiness
from HustleCommon.Dto.PipDto import PipDto as PipDto
from HustleDatabase.Model.Pip.PipDeleteModel import PipDeleteModel as PipDelModel

router = APIRouter()
service = Bussiness()

@router.get('/get-all-pip')
def GetAllPip():
    return service.GetAllPip()

@router.post('/add-pip')
def InputPip(model: PipDto = Body(...)):
    return service.InputPip(model)

@router.delete('/delete-pip')
def DeletePip(model: PipDelModel = Body(...)):
    return service.DeletePip(model)