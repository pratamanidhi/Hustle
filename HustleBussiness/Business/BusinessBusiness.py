from HustleDatabase.Model.Ingredient.CoffeeIngredientModel import CoffeeIngredientModel as CoffeeIngredient
from  HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Table.WarehouseTable import  WarehouseTable as DbContext
from HustleDatabase.Model.Ingredient import  CoffeeIngredientModel as Coffee, TeaIngredientModel as Tea
from HustleCommon.Enums.Ingredient import  Ingredient as Enum
from HustleDatabase.Model.Warehouse import OtherModel as Model

repo = Repo()
dbContext = DbContext()

class BusinessBusiness():
    def __init__(self) -> None:
        pass


    def GetCoffeeIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Coffee, Coffee)
        return ingredient

    def GetTeaIngredient(self):
        ingredient = Repo.GetIngredient(self, dbContext.Tea, Tea)
        return ingredient

    def CalculatePrice(self, business):
        ingredient = sum(business.ingredient) + business.expectedProfit
        return ingredient

    def ImportIngredient(self, csv):
        data = [row for row in csv]
        for datas in data:
            Model.OtherModel.name = datas["Item"]
            Model.OtherModel.price = int(datas["Price"])
            Model.OtherModel.description = datas["Brand"]
            Model.OtherModel.priceUnit = datas["PriceUnit"]
            Model.OtherModel.packaging = int(datas["Packaging"])
            Repo.AddStock(self, dbContext.Other, Model.OtherModel)
        return data


    def GetIngredient(self, types: Enum):
        match types:
            case Enum.Coffee:
                return self.GetCoffeeIngredient()
            case Enum.Tea:
                return self.GetTeaIngredient()
            case _:
                return "Unknown"


