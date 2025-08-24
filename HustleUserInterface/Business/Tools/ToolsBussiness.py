from API.Tools.ToolsAPI import ToolsAPI as ToolsApi

api = ToolsApi()
class ToolsBusiness:
    def __init__(self) -> None:
        pass

    def GetTools(self):
        return api.GetTools()
