from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext
from HustleCommon.Enums.Ingredient import Ingredient as Enum
from HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Model.Warehouse.WarehouseModel import WarehouseModel as Warehouse
from datetime import datetime

repo = Repo()
dbContext = DbContext()

class WarehouseBusiness:
    def __init__(self) -> None:
        self.context_map = {
            Enum.Coffee: (dbContext.Coffee, Warehouse),
            Enum.Juice: (dbContext.Juice, Warehouse),
            Enum.MilkAndCream: (dbContext.MilkAndCream, Warehouse),
            Enum.Other: (dbContext.Other, Warehouse),
            Enum.Powder: (dbContext.Powder, Warehouse),
            Enum.Syrup: (dbContext.Syrup, Warehouse),
            Enum.Tea: (dbContext.Tea, Warehouse),
            Enum.Topping: (dbContext.Topping, Warehouse),
        }

    def GetStock(self, types: Enum):
        if types in self.context_map:
            context, model = self.context_map[types]
            return repo.GetStock(context, model)
        return "No Data"

    def AddStock(self, types: Enum, model):
        if types in self.context_map:
            context, _ = self.context_map[types]
            return repo.AddStock(context, model)
        return "No Data"

    def UpdateStock(self, types: Enum, isOut, model):
        if types in self.context_map:
            context, _ = self.context_map[types]
            checkStock = repo.CheckStock(context, model)

            if isOut:
                model.totalStock = int(checkStock['totalStock']) - model.stockOut
                model.stockIn = checkStock['stockIn']
                if checkStock['stockOut'] is None:
                    checkStock['stockOut'] = 0

                model.stockOut = int(checkStock['stockOut']) + model.stockOut
                model.lastInput = checkStock['lastInput']
                model.lastOutput = datetime.now()
            else:
                model.totalStock = int(checkStock['totalStock']) + model.stockIn
                model.stockIn = model.stockIn
                model.stockOut = checkStock['stockOut']
                model.lastInput = datetime.now()
                model.lastOutput = checkStock['lastOutput']

            return repo.StockUpdate(context, model)
        return "No Data"
