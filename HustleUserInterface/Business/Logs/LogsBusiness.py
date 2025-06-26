from HustleUserInterface.API.Logs.LogsAPI import LogsAPI as Logs

log = Logs()
class LogsBusiness:
    def __init__(self) -> None:
        pass

    def InsertLog(self,data):
        datas = data['data'][0]
        print(f'user: {datas['updatedBy']}')
        print(f'datas: {datas}')

        logsData = {
            "data" : {
                "isOut": data['isOut'],
                "input": datas
            }
        }
        return log.InsertLog(datas['updatedBy'], logsData)