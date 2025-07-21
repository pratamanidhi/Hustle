from HustleDatabase.ConnectionWarehouse import ConnectionWarehouse as Connection
import uuid

db = Connection()
class ToolsRepository():
    def __init__(self) -> None:
        pass

    def GetAllTools(self):
        query = 'select * from Tools'
        result = db.Execute(query)
        return result

    def InsertTools(self, model):
        guid = str(uuid.uuid4())
        query = f'insert into Tools (guid, name, updatedAt) values (?, ?, ?)'
        result = db.Execute(query, (
            guid,
            model.name,
            model.updatedAt
        ))
        return result