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

    def GetDailyLog(self):
        query = f'select * from DailyLog'
        datas = db.Execute(query)
        return datas

    def GetDailyStockByName(self, name):
        query = f'select * from DailyLog where name = ?'
        result = db.Execute(query, (name,))
        if not result:
            return None
        else:
            return dict(result[0])

    def InsertDailyLog(self, model):
        guid = str(uuid.uuid4())
        query = 'INSERT INTO DailyLog(guid, name, stockIn, stockOut, price, timestamp) VALUES (?, ?, ?, ?, ?, ?)'
        result = db.Execute(query, (guid, model.name, model.stockIn, model.stockOut, model.price, model.timestamp))
        return result

    def UpdateDailyStock(self, model, isOut):
        if isOut:
            query = f'update DailyLog set stockOut = ? where name = ?'
            stock = model.stockOut
        else:
            query = f'update DailyLog set stockIn = ? where name = ?'
            stock = model.stockIn
        result = db.Execute(query, (stock, model.name))
        return result
