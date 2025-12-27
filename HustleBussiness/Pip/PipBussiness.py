from HustleCommon.Enums.Ingredient import Ingredient
from HustleDatabase.Repository.Pip.PipRepository import PipRepository as Repository
from HustleDatabase.Model.Pip.PipModel import PipModel as pipModel
from HustleDatabase.Model.Warehouse.WarehouseModel import WarehouseModel as warehouseModel
from HustleBussiness.Warehouse.WarehouseBussiness import WarehouseBusiness as WarehouseBusiness
from HustleBussiness.Unit.UnitBusiness import UnitBusiness as UnitBusiness
import json
import ast

repo= Repository()
whBusiness = WarehouseBusiness()
unitBusiness = UnitBusiness()
whModel = warehouseModel()

class PipBussiness():
    def __init__(self) -> None:
        pass

    def GetAllPip(self):
        result = repo.GetAllPip()
        return result

    def InputPip(self, input):
        try:
            pipModel.name = input.name
            pipModel.ingredient = input.ingredient
            pipModel.price = input.price
            self.inputIntoWarehouse(input)
            result = repo.InputPip(pipModel)
            return result
        except Exception as e:
            return e

    def GetPipByGuid(self, name):
        result = repo.GetPipByGuid(name)
        return result


    def DeletePip(self, model):
        whBusiness.DeletePipStock(model.name)
        return repo.DeletePip(model)

    def inputIntoWarehouse(self, pipInput):
        try:
            ingredients = ast.literal_eval(pipInput.ingredient)

            volume = []
            for ingredient in ingredients:
                volume.append(int(ingredient["doseInput"]))

            totalVolume = sum(volume)
            unit = unitBusiness.GetUnitByName("ml")
            whModel.name = pipInput.name
            whModel.stockIn = totalVolume
            whModel.packaging = totalVolume
            whModel.unit = unit['guid']
            whModel.updatedBy = pipInput.inputedBy
            whModel.price = pipInput.price

            result = whBusiness.AddStock(Ingredient.Pip, whModel)
            print(result)
        except Exception as e:
            return e

