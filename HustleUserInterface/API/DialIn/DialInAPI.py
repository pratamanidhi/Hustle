import requests
from Common.ApiUrl import APIUrl as Api

class DialInAPI:
    def __init__(self) -> None:
        pass

    def GetAllDial(self):
        response = requests.get(Api.getAllDialIn)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def InputDialIn(self, datas):
        try:
            response = requests.post(Api.insertDialIn, json=datas)
            if response.status_code == 200:
                return True
            else:
                return False

        except Exception as e:
            print('Exception occurred: ', e)
            return e
