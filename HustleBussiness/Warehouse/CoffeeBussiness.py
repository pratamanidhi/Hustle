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


