from fastapi import APIRouter, Body
from HustleBussiness.Menu.MenuBusiness import MenuBusiness as Bussiness
from HustleCommon.Dto.MenuDto import MenuDto as MenuDto
from HustleDatabase.Model.Menu.MenuDeleteModel import MenuDeleteModel as MenuDeleteModel

router = APIRouter()
service = Bussiness()

@router.get('/get-menu')
def GetMenu():
    return service.GetMenu()

@router.post('/add-menu')
def InputMenu(model: MenuDto = Body(...)):
    return service.InputMenu(model)

@router.delete('/delete-menu')
def DeleteMenu(model: MenuDeleteModel = Body(...)):
    return service.DeleteMenu(model)