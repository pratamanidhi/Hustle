from API.Menu.MenuAPI import MenuAPI as Api

api = Api()
class MenuBusiness():
    def __init__(self) -> None:
        pass

    def InputMenu(self, data):
        return api.InputMenu(data)

    def GetMenu(self):
        return api.GetMenu()

    def DeleteMenu(self, name):
        datas = {
            "name": name
        }
        return api.DeleteMenu(datas)