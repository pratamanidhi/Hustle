from fastapi import FastAPI
from HustleController import CoffeeMenuController, MilkBaseMenuController, CameraController, UserManagementController
from HustleController.Warehouse import  WarehouseController
from HustleController.Business import BusinessController
from HustleController.Enums import IngredientController
import uvicorn

app = FastAPI()
app = FastAPI(
    title="Hustle API",  # <- Set your custom title here
    description="API for managing coffee, milk base, camera, users, and warehouse operations.",
    version="1.0.0"
)

app.include_router(CoffeeMenuController.router, prefix="/coffee", tags=["Coffee Menu"])
app.include_router(MilkBaseMenuController.router, prefix="/milkbase", tags=["Milk Base"])
app.include_router(CameraController.router, prefix="/device", tags=["Device"])
app.include_router(UserManagementController.router, prefix="/users", tags=["User Management"])
app.include_router(BusinessController.router, prefix="/business", tags=["Business"])
app.include_router(WarehouseController.router, prefix="/warehouse", tags=["Warehouse Coffee"])
app.include_router(IngredientController.router, prefix="/enum", tags=["Enum"])

if __name__ == "__main__":
    uvicorn.run("Main-Backend:app", host="127.0.0.1", port=8000, reload=True)