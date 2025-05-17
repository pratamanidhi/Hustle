from HustleDatabase.Connection import Connection
from HustleDatabase.Model.MilkBaseModel import MilkBase
import uuid

class MilkBaseRepo():
    def __init__(self) -> None:
        pass

    def GetAllMilkBase(self):
        db = Connection()
        milkBases = db.FetchAll('SELECT * FROM "Menu.MilkBase"', MilkBase)
        return milkBases

    def AddMilkBase(self, milkBase):
        db = Connection()
        guid = str(uuid.uuid4())
        query = 'INSERT INTO "Menu.MilkBase" (guid, name, price) VALUES (?, ?, ?)'
        result = db.Execute(query, (guid, milkBase.name, milkBase.price))
        return result