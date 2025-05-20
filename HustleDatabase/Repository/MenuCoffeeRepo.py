from HustleDatabase.Connection import Connection
from HustleDatabase.Model.CoffeeModel import Coffee
import uuid

class MenuCoffeeRepo():
    def __init__(self) -> None:
            pass


    def GetAllCoffee(self):
        db = Connection()
        coffees = db.FetchAll('SELECT * FROM "Menu.Coffee"', Coffee)
        return coffees


    def AddCoffee(self, coffee):
        db = Connection()
        guid = str(uuid.uuid4())
        query = 'INSERT INTO "Menu.Coffee" (guid, name, price) VALUES (?, ?, ?)'
        result = db.Execute(query, (guid, coffee.name, coffee.price))
        return result





