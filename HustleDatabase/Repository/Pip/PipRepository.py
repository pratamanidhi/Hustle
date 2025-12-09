import uuid
from datetime import datetime, date
from HustleDatabase.Connection import Connection
from HustleDatabase.Model.Pip.PipModel import PipModel

db = Connection()

class PipRepository():
    def __init__(self) -> None:
        pass

    def GetAllPip(self):
        query = "select * from Pip"
        result = db.Execute(query)
        return result

    def InputPip(self, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = "insert into Pip (guid, name, ingredient, price, lastUpdated) values (?, ?, ?, ?, ?)"
        result = db.Execute(query, (
            guid,
            model.name,
            model.ingredient,
            model.price,
            updatedAt
        ))
        return result

    def DeletePip(self, model):
        query = "delete from pip where name = ?"
        result = db.Execute(query, (model.name, ))
        return result