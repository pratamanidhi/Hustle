import requests
from Common.ApiUrl import APIUrl as  Api

class PipAPI():
    def __init__(self) -> None:
        pass

    def InputPip(self, datas):
        try:
            response = requests.post(Api.inputPip, json=datas)
            if response.status_code == 200:
                return True
            else:
                return None
        except Exception as e:
            print(e)

    def GetPip(self):
        try:
            response = requests.get(Api.getPip)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(e)

    def DeletePip(self, datas):
        try:
            response = requests.delete(Api.deletePip, json=datas)
            if response.status_code == 200:
                return True
            else:
                return None
        except Exception as e:
            print(e)