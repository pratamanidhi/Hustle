from fastapi import APIRouter
from HustleDevice.Camera import Camera as Cam

router = APIRouter()
service = Cam()

@router.get("/start-camera")
def StartCamera():
    return service.StartCamera()

@router.get("/stop-camera")
def StopCamera():
    return service.StopCamera()