from HustleDatabase.Repository.Pip.PipRepository import PipRepository as Repository
from HustleDatabase.Model.Pip.PipModel import PipModel as pipModel

repo= Repository()

class PipBussiness():
    def __init__(self) -> None:
        pass

    def GetAllPip(self):
        result = repo.GetAllPip()
        return result

    def InputPip(self, input):
        pipModel.name = input.name
        pipModel.ingredient = input.ingredient
        pipModel.price = input.price
        result = repo.InputPip(pipModel)
        return result

    def DeletePip(self, model):
        return repo.DeletePip(model)