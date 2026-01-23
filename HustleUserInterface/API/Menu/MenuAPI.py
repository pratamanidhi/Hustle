import requests
from Common.ApiUrl import APIUrl as  Api

class MenuAPI():
    def __init__(self) -> None:
        pass

    def GetMenu(self):
        response = requests.get(Api.getMenu)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def InputMenu(self, datas):
        try:
            response = requests.post(Api.inputMenu, json=datas)
            if response.status_code == 200:
                return True
            else:
                return None
        except Exception as e:
            print(e)

