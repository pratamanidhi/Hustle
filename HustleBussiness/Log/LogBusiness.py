from HustleDatabase.Model.Logs.LogModel import LogModel as Model
from HustleDatabase.Repository.Logs.LogRepository import LogRepository as Repository
from datetime import datetime

repo = Repository()
model = Model()
class LogBusiness():
    def __init__(self) -> None:
        pass

    def GetLogs(self):
        return repo.GetLog()

    def InsertLog(self, model):
        model.timestamp = datetime.now()
        return repo.InsertLog(model)