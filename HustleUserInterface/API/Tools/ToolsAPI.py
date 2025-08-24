import requests
from Common.ApiUrl import APIUrl as Api

class ToolsAPI:
    def __init__(self) -> None:
        pass

    def GetTools(self):
        try:
            response = requests.get(Api.getAllTools)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed with status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Exception occurred: {e}")
            return None
