from HustleDatabase.Repository.UserManagementRepo import  UserManagementRepo as UserManagement

UserMgmt = UserManagement()
class UserManagementBussiness():
    def __init__(self) -> None:
        pass

    def UserLogin(self, user):
        loginResult = UserMgmt.UserLogin(user)
        return loginResult

    def GetAllUser(self):
        return UserMgmt.GetAllUser()

    def AddUser(self, model):
        result = UserMgmt.AddUserAccount(model)
        return result
