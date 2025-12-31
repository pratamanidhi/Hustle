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

    def DeleteUser(self, model):
        result = UserMgmt.DeleteUserAccount(model)
        return result

    def UpdateUser(self, model):
        result = UserMgmt.UpdateUserAccount(model)
        return result
