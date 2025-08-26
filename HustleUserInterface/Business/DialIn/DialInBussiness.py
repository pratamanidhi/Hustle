from API.DialIn.DialInAPI import  DialInAPI as Api


api = Api()
class DialInBussiness:
    def __init__(self) -> None:
        pass

    def GetAllDialIn(self):
        return api.GetAllDial()

    def InputDialIn(self, input):
        return api.InputDialIn(input)
