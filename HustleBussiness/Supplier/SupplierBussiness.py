
from HustleDatabase.Repository.Supplier.SupplierRepository import SupplierRepository as Repository
from HustleDatabase.Model.Supplier.SupplierModel import SupplierModel as Model
from HustleDatabase.Model.Supplier.OrderTypeModel import OrderTypeModel as OrderModel
from HustleDatabase.Model.Supplier.BankAccountModel import BankAccountModel as BankAccountModel
from HustleDatabase.Model.Supplier.ReceiveOrderModel import ReceiveOrderModel as ReceiveOrderModel
from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext

repo = Repository()
model = Model()
orderModel = OrderModel()
bankModel = BankAccountModel()
receiveOrderModel = ReceiveOrderModel()
dbContext = DbContext()

class SupplierBussiness():
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self):
        result = repo.GetAllSupplier(dbContext.Supplier)
        return result

    def GetSupplierWithCategory(self, input):
        result = self.GetSupplierFilteredByCategory(input)
        return result

    def InputSupplier(self, input):
        model.name = input.name
        model.orderType = self.SupplierTypeId(input.orderType)['guid']
        model.bankAccount = self.BankAccountId(input)['guid']
        model.contactPerson = input.contactPerson
        model.productName = input.productName

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

    def SupplierTypeId(self, name):
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

    def GetSupplierFilteredByCategory(self, category):
        categoryGuid = repo.GetSupplierId(dbContext.OrderType, category)
        result = repo.GetSupplierWithCategory(dbContext.Supplier, categoryGuid['guid'])
        return result

    def InputOrder(self, datas):
        receiveOrderModel.supplierId = datas.supplierId
        receiveOrderModel.quantity = datas.quantity
        result = repo.InputReceiveOrder(dbContext.ReceivedOrder, receiveOrderModel)
        return result



