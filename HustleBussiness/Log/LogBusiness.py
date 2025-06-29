from HustleDatabase.Repository.Logs.LogRepository import LogRepository as Repository
from datetime import datetime

repo = Repository()
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