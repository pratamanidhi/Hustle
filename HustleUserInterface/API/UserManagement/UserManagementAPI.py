import requests
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class UserManagementAPI:
    def __init__(self) -> None:
        pass

    def Login(self, username, password):
        try:
            params = {
                'username': username,
                'password': password
            }
            response = requests.post(Api.login, json=params)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None
        except Exception as e:
            print(e)
            return e