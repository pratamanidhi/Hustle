from fastapi import APIRouter, Body
from HustleBussiness.UserManagementBussiness import UserManagementBussiness as UserManagement
from HustleDatabase.Model.UserLogin import UserLogin as Login
from HustleDatabase.Model.UserMgmt.AddUserModel import AddUserModel as AddUser

router = APIRouter()
service = UserManagement()

@router.post("/user-login")
def UserLogin(user : Login):
    return service.UserLogin(user)

@router.post("/add-user")
def AddUser(model: AddUser = Body(...)):
    return service.AddUser(model)


@router.get("/get-all-user")
def GetAlluser():
    return service.GetAllUser()