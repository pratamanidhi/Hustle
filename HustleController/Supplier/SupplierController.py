from fastapi import APIRouter, Body
from HustleBussiness.Supplier.SupplierBussiness import SupplierBussiness as Business
from HustleCommon.Dto.SupplierDto import SupplierDto as SupplierDto
from HustleCommon.Dto.OrderTypeDto import OrderTypeDto as OrderTypeDto
from HustleCommon.Dto.SupplierByCategoryDto import SupplierByCategoryDto as SupplierByCategoryDto
from HustleCommon.Dto.BankAccountDto import BankAccountDto as BankAccountDto
from HustleCommon.Dto.ReceiveOrderDto import ReceiveOrderDto as ReceiveOrderDto

router = APIRouter()
service = Business()

@router.get('/get-all-supplier')
def GetAllSupplier():
    return service.GetAllSupplier()

@router.post('/get-supplier-by-category')
def GetSupplierByCategory(model: SupplierByCategoryDto = Body(...)):
    return service.GetSupplierWithCategory(model)

@router.post('/add-supplier')
def InsertSupplier(model: SupplierDto = Body(...)):
    return service.InputSupplier(model)

@router.get('/supplier-type')
def GetSupplierType():
    return service.GetAllSupplierType()

@router.post('/add-supplier-type')
def InputSupplierType(model: OrderTypeDto = Body(...)):
    return service.InputSupplierType(model)

@router.get('/get-bank-account')
def GetBankAccount():
    return service.GetAllBankAccount()

@router.post('/add-bank-account')
def InputBankAccount(model: BankAccountDto = Body(...)):
    return service.InputBankAccount(model)

@router.post('/receive-order')
def ReceiveOrder(model: ReceiveOrderDto = Body(...)):
    return service.InputOrder(model)

