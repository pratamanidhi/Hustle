from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext
from HustleDatabase.Repository.Unit.UnitRepository import UnitRepository as Repo

repo = Repo()
dbContext = DbContext

class UnitBusiness:
    def __init__(self) -> None:
        pass

    def GetUnit(self):
        return repo.GetUnit(DbContext.Unit)

    def GetUnitByName(self, param):
        return repo.GetUnitByName(DbContext.Unit, param)