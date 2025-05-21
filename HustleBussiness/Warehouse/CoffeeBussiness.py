from HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Table.WarehouseTable import  WarehouseTable as DbContext
from HustleDatabase.Model.Warehouse.CoffeeModel import CoffeeModel as Coffee

repo = Repo()
dbContext = DbContext()
class CoffeeBusiness():
    def __init__(self) -> None:
        pass

    def GetStock(self):
        stock = Repo.GetStock(self, dbContext.Coffee, Coffee)
        return stock

    def AddStock(self, coffee):
        result = Repo.AddStock(self, dbContext.Coffee, coffee)
        return result

    def UpdateStock(self, isOut, coffee):
        result = Repo.StockUpdate(self, dbContext.Coffee, isOut, coffee)
        return result



