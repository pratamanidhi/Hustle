from API.Common.CommonAPI import CommonApi as CommonApi
from API.Unit.UnitAPI import UnitAPI as Unit

common = CommonApi()
unit = Unit()
class CommonBusiness():
    def __init__(self) -> None:
        pass

    def GetIngredient(self):
        return common.Category()

    def GetUnit(self):
        return unit.GetAllUnit()