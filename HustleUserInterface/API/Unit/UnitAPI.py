from http.client import responses

import requests
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class UnitAPI:
    def __init__(self) -> None:
        pass

    def GetAllUnit(self):
        try:
            response = requests.get(Api.getAllUnit)
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except Exception as e:
            print(f'Exception: {e}')
            return None

    def GetUnitByName(self, param):
        try:
            params = {
                'param': param
            }
            response = requests.get(Api.getUnitBytName, params)
            if response.status_code == 200:
                return response.json()
            else:
                return False

        except Exception as e:
            print(f'Exception: {e}')
            return None