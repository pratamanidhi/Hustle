
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
        model.orderType = self.SupplierTypeid(input.orderType)['guid']
        model.bankAccount = self.BankAccountId(input)['guid']
        model.contactPerson = input.contactPerson

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

    def SupplierTypeid(self, name):
        result = repo.GetSupplierId(dbContext.OrderType, name)

        if result is None:
            orderModel.name = name
            input = repo.InsertSupplierType(dbContext.OrderType, orderModel)
            return input
        else:
            return result


    def BankAccountId(self, model):
        result = repo.GetBankNumberId(dbContext.BankAccount, model)
        print(result)

        if result is None:
            input = repo.InputBankNumber(dbContext.BankAccount, model)
            return input
        else:
            return result



