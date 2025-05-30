from HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext
from HustleDatabase.Model.Ingredient.IngredientModel import IngredientModel as Model
from HustleCommon.Enums.Ingredient import Ingredient as Enum

repo = Repo()
dbContext = DbContext()

class BusinessBusiness:
    def __init__(self) -> None:
        self.context_map = {
            Enum.Coffee: dbContext.Coffee,
            Enum.Juice: dbContext.Juice,
            Enum.MilkAndCream: dbContext.MilkAndCream,
            Enum.Other: dbContext.Other,
            Enum.Powder: dbContext.Powder,
            Enum.Syrup: dbContext.Syrup,
            Enum.Tea: dbContext.Tea,
            Enum.Topping: dbContext.Topping,
        }

    def GetIngredient(self, types: Enum):
        if types in self.context_map:
            return repo.GetIngredient(self.context_map[types], Model)
        return "Unknown"

    def CalculatePrice(self, business):
        return sum(business.ingredient) + business.expectedProfit
