import requests
from Common.ApiUrl import APIUrl as Api

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

    def GetAllUser(self):
        try:
            response = requests.get(Api.getAllUser)
            if response.status_code == 200:
                return response.json()
            else:
                print("Error with status code:", response.status_code)
                return None
        except Exception as e:
            print("Exception occurred: ", e)
            return e
