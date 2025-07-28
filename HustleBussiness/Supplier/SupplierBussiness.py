
from HustleDatabase.Repository.Supplier.SupplierRepository import SupplierRepository as Repository
from HustleDatabase.Model.Supplier.SupplierModel import SupplierModel as Model
from HustleDatabase.Model.Supplier.OrderTypeModel import OrderTypeModel as OrderModel
from HustleDatabase.Model.Supplier.BankAccountModel import BankAccountModel as BankAccountModel
from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext

repo = Repository()
model = Model()
orderModel = OrderModel()
bankModel = BankAccountModel()
dbContext = DbContext()

class SupplierBussiness():
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self):
        result = repo.GetAllSupplier(dbContext.Supplier)
        return result

    def InputSupplier(self, input):
        model.name = input.name
        model.orderType = input.orderType
        model.bankNumber = input.bankNumber
        model.bankName = input.bankName
        model.contactPerson = input.contactPerson
        print("input", input)
        print("model", model)

        result = repo.InsertSupplier(dbContext.Supplier, model)
        return result

    def GetAllSupplierType(self):
        result = repo.GetAllSupplierType(dbContext.OrderType)
        return result

    def InputSupplierType(self, input):
        orderModel.name = input.name

        result = repo.InsertSupplierType(dbContext.OrderType, orderModel)
        return result

    def GetAllBankAccount(self):
        result = repo.GetAllBankNumber(dbContext.BankAccount)
        return result

    def InputBankAccount(self, input):
        bankModel.name = input.name
        bankModel.bankNumber = input.bankNumber

        result = repo.InputBankNumber(dbContext.BankAccount, bankModel)
        return result

