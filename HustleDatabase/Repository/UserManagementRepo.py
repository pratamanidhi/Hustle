from HustleDatabase.Connection import Connection
from HustleDatabase.Model import UserLogin, UserManagement

class UserManagementRepo():
    def __init__(self) -> None:
        pass

    def UserLogin(self, login):
        db = Connection()
        query = 'SELECT * FROM "User.Management" WHERE username = ? AND password = ?'
        result = db.Execute(query, (login.username, login.password))
        return dict(result[0]) if result else {}