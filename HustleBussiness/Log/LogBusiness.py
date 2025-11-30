from HustleCommon.Enums.Ingredient import Ingredient
from HustleDatabase.Repository.Logs.LogRepository import LogRepository as Repository
from HustleDatabase.Table.LogTable import LogTable as DbContext
from datetime import datetime, date

repo = Repository()
dbContext = DbContext()
class LogBusiness():
    def __init__(self) -> None:
        pass

    def GetLogs(self):

        result = repo.GetLog()
        return result

    def InsertLog(self, model):
        model.timestamp = datetime.now()
        return repo.InsertLog(model)

    def GetDailyLogByName(self, name):
        result = repo.GetDailyStockByName(name)
        return result

    def InsertDailyLog(self, dailyLogModel):
        dailyLogModel.timestamp = datetime.now()
        return repo.InsertDailyLog(dailyLogModel)

    def UpdateDailyStock(self, model, isOut):
        return repo.UpdateDailyStock(model, isOut)

    def GetReportByCategory(self, types):
        category = Ingredient(types).name
        return repo.GetReportByCategory(dbContext.DailyStock, category)

    def GetAllReport(self):
        datas = []
        for category in Ingredient:
            data = {
                'name' : Ingredient(category).name,
                'data' : repo.GetReportByCategory(dbContext.DailyStock, Ingredient(category).name)
            }
            datas.append(data)
        return datas

    def GetReportByPeriod(self, start, end):
        datas = []
        for category in Ingredient:
            data = {
                'name' : Ingredient(category).name,
                'data' : repo.GetReportByCategoryAndPeriod(dbContext.DailyStock, Ingredient(category).name, start, end)
            }
            datas.append(data)
        return datas



    def InputIntoDailyStockReport(self, model):
        model.datetime = date.today().isoformat()
        model.lastUpdated = datetime.now()
        checkReport = self.CheckDailyReport(model)

        if checkReport is not None:
            if model.stockIn is None or model.stockIn == int(checkReport["stockIn"]):
                model.stockIn = 0

            if model.stockOut is None or model.stockOut == int(checkReport["stockOut"]):
                model.stockOut = 0

            model.totalStockTransaction = int(model.stockIn) + int(model.stockOut)



        if checkReport is not None:
            model.guid = checkReport["guid"]
            model.stockOut = int(model.stockOut) + int(checkReport["stockOut"])
            model.stockIn = int(model.stockIn) + int(checkReport["stockIn"])
            model.totalStockTransaction = int(model.totalStockTransaction) + int(checkReport["totalStockTransaction"])
            return repo.UpdateDailyReport(dbContext.DailyStock, model)
        else:
            return repo.InsertIntoDailyReport(dbContext.DailyStock, model)

    def CheckDailyReport(self, model):
        return repo.CheckDailyReport(dbContext.DailyStock, model)