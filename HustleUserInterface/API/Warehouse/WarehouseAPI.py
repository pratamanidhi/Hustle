import requests
from nicegui.html import param

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
                return data
            else:
                print(f"Failed with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Exception occurred: {e}")
            return None

    def GetAllStock(self):
        try:
            response = requests.get(Api.getAllWarehouse)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Exception occurred: {e}")
            return None

    def AddStock(self, value):
        try:
            print(value)
            param = {'types': value['type']}
            response = requests.post(Api.addStock, params=param, json=value['data'])
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception: {e}")
            return None

    def CheckOutStock(self, type, isOut, datas):
        try:
            param = {
                'types' : type,
                'isOut' : str(isOut).lower()
            }

            response = requests.put(Api.checkOutStock, params=param, json=datas)
            print(response)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(f'Exception occured: {e}')
            return None

    def DeleteStock(self, type, guid):
        try:
            param = {
                'types': type
            }

            guid = {
                'guid': guid
            }

            response = requests.delete(Api.deleteStock, params=param, json=guid)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(f'Exception occured: ', e)
            return None



