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

    def CheckDailyReport(self, table, model):
        query = f"select * from {table} where name = ? and datetime = ?"
        result = db.Execute(query, (model.name, model.datetime))
        if not result:
            return None
        else:
            return dict(result[0])

    def GetReportByCategory(self, table, category):
        query = f'select guid,name,SUM(stockOut) AS stockOut,SUM(stockIn) AS stockIn,SUM(totalStockTransaction) AS totalStockTransaction, category, datetime, MAX(lastUpdated) AS lastUpdated from {table} where category = ? GROUP BY name, category ORDER BY name'
        result = db.Execute(query, (category,))
        return result

    def GetReportByCategoryAndPeriod(self, table, category, start, end):
        query = f'select guid,name,SUM(stockOut) AS stockOut,SUM(stockIn) AS stockIn,SUM(totalStockTransaction) AS totalStockTransaction, category, MAX(datetime) as datetime, MAX(lastUpdated) AS lastUpdated from {table} where category = ?   AND datetime >= ? AND datetime <  ? GROUP BY name, category ORDER BY name'
        result = db.Execute(query, (category, start, end))
        return result

    def InsertIntoDailyReport(self, table, model):
        guid = str(uuid.uuid4())
        query = f"insert into {table} (guid, name, stockOut, stockIn, totalStockTransaction, category, datetime, lastUpdated) values (?, ?, ?, ?, ?, ?, ?, ?)"
        result = db.Execute(query, (guid, model.name, model.stockOut, model.stockIn, model.totalStockTransaction, model.category, model.datetime, model.lastUpdated))
        return result

    def UpdateDailyReport(self, table, model):
        query = f"update {table} set stockOut = ?, stockIn = ?, totalStockTransaction = ?, lastUpdated = ? where guid = ?"
        result = db.Execute(query, (model.stockOut, model.stockIn, model.totalStockTransaction, model.lastUpdated, model.guid))
        return result
