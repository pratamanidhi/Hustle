import requests
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class BusinessAPI:
    def __init__(self) -> None:
        pass

    def GetIngredient(self, type):
        param = {
            "types": type
        }
        response = requests.get(Api.ingredient, params=param)

        if response.status_code == 200:
            return response.json()
        else:
            return None