import requests
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class SupplierAPI:
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self):
        response = requests.get(Api.getAllSupplier)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def GetAllSupplierCategory(self):
        response = requests.get(Api.getAllSupplierCategory)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def InputSupplier(self, datas):
        try:
            response = requests.post(Api.inputSupplier, json=datas)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print('Exception occurred: ', e)
            return e

    def GetSupplierByCategory(self, body):
        try:
            response = requests.post(Api.getSupplierByCategory, json=body)
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except Exception as e:
            print('Exception occurred: ', e)
            return e