from fastapi import FastAPI
from HustleController import CoffeeMenuController, MilkBaseMenuController, CameraController, UserManagementController
from HustleController.Warehouse import  CoffeeController
import uvicorn

app = FastAPI()

app.include_router(CoffeeMenuController.router)
app.include_router(MilkBaseMenuController.router)
app.include_router(CameraController.router)
app.include_router(UserManagementController.router)

app.include_router(CoffeeController.router)

if __name__ == "__main__":
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)