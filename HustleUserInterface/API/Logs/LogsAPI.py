import requests
from HustleUserInterface.Common.ApiUrl import APIUrl as Api

class LogsAPI:
    def __init__(self) -> None:
        pass

    def InsertLog(self, user, data):
        try:
            datas = {
                "user": user,
                "action": str(data)
            }
            print(datas)
            response = requests.post(Api.insertLogs, json=datas)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception occured: {e}")