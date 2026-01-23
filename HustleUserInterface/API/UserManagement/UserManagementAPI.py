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

    def InputNewUser(self, data):
        try:
            response = requests.post(Api.addUser, json=data)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print("Exception occurred: ", e)
            return e

    def DeleteUser(self, data):
        try:
            response = requests.delete(Api.deleteUser, json=data)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print("Exception occurred: ", e)
            return e

    def UpdateUser(self, data):
        try:
            response = requests.put(Api.updateUser, json=data)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print("Exception occurred: ", e)
            return e