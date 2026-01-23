from fastapi import APIRouter, Body
from HustleBussiness.Menu.MenuBusiness import MenuBusiness as Bussiness
from HustleCommon.Dto.MenuDto import MenuDto as MenuDto

router = APIRouter()
service = Bussiness()

@router.post('/add-menu')
def InputMenu(model: MenuDto = Body(...)):
    return service.InputMenu(model)