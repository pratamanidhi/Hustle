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
            print('param', params)
            response = requests.post(Api.login, json=params)
            if response.status_code == 200:
                data = response.json()
                print(data)
                return data
            else:
                return None
        except Exception as e:
            print(e)
            return e