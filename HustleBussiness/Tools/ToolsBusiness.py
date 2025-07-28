from HustleDatabase.Repository.Tools.ToolsRepository import ToolsRepository as Repository
from HustleDatabase.Model.Tools.ToolsModel import ToolsModel as Model
from datetime import datetime

repo = Repository()
model = Model()
class ToolsBusiness():
    def __init__(self) -> None:
        pass

    def GetAllTools(self):
        return repo.GetAllTools()

    def InputTools(self, input):
        model.name = input.name
        model.updatedAt = str(datetime.now())
        result = repo.InsertTools(model)
        return result