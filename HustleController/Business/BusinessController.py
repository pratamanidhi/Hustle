from fastapi import APIRouter, File, UploadFile
import csv
from io import StringIO
from HustleBussiness.Business.BusinessBusiness import BusinessBusiness as BusinessService
from HustleDatabase.Model.Business.BusinessModel import BusinessModel as Business
from HustleCommon.Enums.Ingredient import Ingredient as Ingredient

router = APIRouter()
service = BusinessService()

@router.post("/calculate-price")
def CalculatePrice(business : Business):
    result = service.CalculatePrice(business)
    return result

@router.get("/coffee-ingredient")
def GetIngredient(types: Ingredient):
    result = service.GetIngredient(types)
    return result

@router.post("/upload-file")
async def UploadFile(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        return {"only csv allowed"}

    contents = await file.read()
    text = contents.decode('utf-8')

    file = StringIO(text)
    reader = csv.DictReader(file)
    result = service.ImportIngredient(reader)
    return {"row": result}

