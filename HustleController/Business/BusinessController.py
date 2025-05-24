from fastapi import  APIRouter
from HustleBussiness.Business.BusinessBusiness import BusinessBusiness as BusinessService
from HustleDatabase.Model.Business.BusinessModel import BusinessModel as Business

router = APIRouter()
service = BusinessService()

@router.post("/calculate-price")
def CalculatePrice(business : Business):
    result = service.CalculatePrice(business)
    return result