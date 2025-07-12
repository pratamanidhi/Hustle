import requests
from Common.ApiUrl import APIUrl as Api

class ReportApi:
    def __init__(self) -> None:
        pass

    def GetReport(self, types):
        param = {
            "types": types
        }
        response = requests.get(Api.getReport, param)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def GetAllReport(self):
        response = requests.get(Api.getAllReport)
        if response.status_code == 200:
            return response.json()
        else:
            return None