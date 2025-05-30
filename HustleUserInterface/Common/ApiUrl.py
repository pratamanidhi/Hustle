from HustleUserInterface.Common.ApiEnum import Enum as Enum

class APIUrl:
    mainiUrl = 'http://localhost:8000'
    warehouse = mainiUrl + f"/{Enum.Warehouse}/get-stock"
    login = mainiUrl + f"/{Enum.UserManagement}/user-login"