import uuid
from datetime import datetime, date
from HustleDatabase.Connection import Connection

db = Connection()

class MenuRepository():
    def __init__(self) -> None:
        pass

    def InputMenu(self, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = "insert into Menu (guid, name, ingredient, price, category, lastUpdate) values (?, ?, ?, ?, ?, ?)"
        result = db.Execute(query, (
            guid,
            model.name,
            model.ingredient,
            model.price,
            model.category,
            updatedAt
        ))
        return result