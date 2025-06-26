from HustleDatabase.ConnectionLog import ConnectionLogs as Connection
import uuid

db = Connection()
class LogRepository():
    def __init__(self) -> None:
        pass


    def GetLog(self):
        query = f'select * from Log'
        logs = db.Execute(query)
        return logs

    def InsertLog(self, model):
        guid = str(uuid.uuid4())
        query = f'INSERT INTO Log (guid, user, action, timestamp) VALUES (?, ?, ?, ?)'
        result = db.Execute(query, (guid, model.user, model.action, model.timestamp))
        return result
