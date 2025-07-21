from HustleDatabase.Connection import Connection
from HustleDatabase.Model import UserLogin, UserManagement
from datetime import datetime


db = Connection()
class UserManagementRepo():
    def __init__(self) -> None:
        pass

    def UserLogin(self, login):
        query = 'SELECT * FROM "User.Management" WHERE username = ? AND password = ?'
        result = db.Execute(query, (login.username, login.password))
        if result and result[0] is not None:
            if self.UpdateLoginData(login, True):
                return dict(result[0])
            else:
                return False
        else:
            return False

    def GetAllUser(self):
        query = 'select * from "User.Management" where isAdmin = 0'
        result = db.Execute(query)
        return result

    def UpdateLoginData(self, login, isLogin):
        if isLogin:
            query = 'Update "User.Management" set lastLogin = ? where username = ?'
        else:
            query = 'Update "User.Management" set lastLogout = ? where username = ?'
        db.Execute(query, (datetime.now(), login.username))
        return True