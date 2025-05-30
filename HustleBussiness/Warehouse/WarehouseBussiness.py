from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext
from HustleCommon.Enums.Ingredient import Ingredient as Enum
from HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Model.Warehouse.WarehouseModel import WarehouseModel as Warehouse

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
            return repo.StockUpdate(context, isOut, model)
        return "No Data"
