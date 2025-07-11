from API.Report.ReportAPI import ReportApi as Api

api = Api()
class ReportBusiness:
    def __init__(self) -> None:
        pass

    def GetReport(self, type):
        return api.GetReport(type)