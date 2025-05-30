from  HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Table.WarehouseTable import  WarehouseTable as DbContext
from HustleDatabase.Model.Ingredient.IngredientModel import IngredientModel as Model
from HustleCommon.Enums.Ingredient import  Ingredient as Enum

repo = Repo()
dbContext = DbContext()

class BusinessBusiness():
    def __init__(self) -> None:
        pass


    def GetCoffeeIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Coffee, Model)
        return ingredient

    def GetJuiceIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Juice, Model)
        return ingredient

    def GetMilkAndCreamIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.MilkAndCream, Model)
        return ingredient

    def GetOtherIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Other, Model)
        return ingredient

    def GetPowderIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Powder, Model)
        return ingredient

    def GetSyrupIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Syrup, Model)
        return ingredient

    def GetTeaIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Tea, Model)
        return ingredient

    def GetToppingIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Topping, Model)
        return ingredient

    def CalculatePrice(self, business):
        ingredient = sum(business.ingredient) + business.expectedProfit
        return ingredient

    def GetIngredient(self, types: Enum):
        match types:
            case Enum.Coffee:
                return self.GetCoffeeIngredient()
            case Enum.Juice:
                return self.GetJuiceIngredient()
            case Enum.MilkAndCream:
                return self.GetMilkAndCreamIngredient()
            case Enum.Other:
                return self.GetOtherIngredient()
            case Enum.Powder:
                return self.GetPowderIngredient()
            case Enum.Syrup:
                return self.GetSyrupIngredient()
            case Enum.Tea:
                return self.GetTeaIngredient()
            case Enum.Topping:
                return self.GetToppingIngredient()
            case _:
                return "Unknown"


