from API.UserManagement.UserManagementAPI import UserManagementAPI as Api

api = Api()
class UserBusiness():

    def __init__(self) -> None:
        pass

    def Login(self, username, password):
        return api.Login(username, password)
