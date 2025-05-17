from fastapi import APIRouter
from HustleBussiness.UserManagementBussiness import UserManagementBussiness as UserManagement
from HustleDatabase.Model.UserLogin import UserLogin as Login

router = APIRouter()
service = UserManagement()

@router.post("/user-login")
def UserLogin(user : Login):
    return service.UserLogin(user)