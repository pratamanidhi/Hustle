import requests
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class CommonApi:
    def __init__(self) -> None:
        pass

    def Category(self):
        response = requests.get(Api.ingredientEnum)
        if response.status_code == 200:
            return response.json()
        else:
            return None
