from fastapi import APIRouter
from HustleCommon.Enums.Ingredient import Ingredient as Ingredient
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ingredient")
def GetIngredient():
    return [
        {"name": i.name, "value": i.value}
        for i in Ingredient
    ]