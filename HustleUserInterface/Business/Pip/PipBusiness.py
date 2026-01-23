from API.Pip.PipAPI import PipAPI as Api

api = Api()
class PipBusiness():
    def __init__(self) -> None:
        pass

    def InputPip(self, data):
        return api.InputPip(data)

    def GetPip(self):
        return api.GetPip()

    def DeletePip(self, name):
        datas = {
            "name": name
        }
        return api.DeletePip(datas)