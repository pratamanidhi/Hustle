from HustleDatabase.ConnectionWarehouse import ConnectionWarehouse as Connection

class UnitRepository:
    def __init__(self) -> None:
        pass

    def GetUnit(self, table):
        db = Connection()
        query = f'select * from {table}'
        unitResult = db.Execute(query)
        return unitResult

    def GetUnitByName(self, table, name):
        db = Connection()
        query = f'''select * from {table} where name = ?'''
        result = db.Execute(query, (name,))
        return dict(result[0])