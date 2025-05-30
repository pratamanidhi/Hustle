import requests
import json
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class WarehouseAPI:
    def __init__(self) -> None:
        pass

    def GetStock(self, type):
        try:
            params = {'types': type}
            response = requests.get(Api.warehouse, params)
            if response.status_code == 200:
                data = response.json()
                print(data)
                return data
            else:
                print(f"Failed with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Exception occurred: {e}")
            return None
