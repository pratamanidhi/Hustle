from fastapi import FastAPI
import uvicorn
from HustleController import CoffeeMenuController, MilkBaseMenuController, CameraController, UserManagementController
from HustleController.Warehouse import WarehouseController
from HustleController.Business import BusinessController
from HustleController.Enums import IngredientController
from HustleController.Unit import UnitController
from HustleController.Log import LogController
from HustleController.Report import ReportController
from HustleController.DialIn import DialInController
from HustleController.Supplier import SupplierController
from HustleController.Pip import PipController

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hustle API",
    description="API for managing coffee, milk base, camera, users, and warehouse operations.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict: ["http://127.0.0.1:5500", "http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(CoffeeMenuController.router, prefix="/coffee", tags=["Coffee Menu"])
app.include_router(MilkBaseMenuController.router, prefix="/milkbase", tags=["Milk Base"])
app.include_router(CameraController.router, prefix="/device", tags=["Device"])
app.include_router(UserManagementController.router, prefix="/users", tags=["User Management"])
app.include_router(BusinessController.router, prefix="/business", tags=["Business"])
app.include_router(WarehouseController.router, prefix="/warehouse", tags=["Warehouse Coffee"])
app.include_router(IngredientController.router, prefix="/enum", tags=["Enum"])
app.include_router(UnitController.router, prefix="/unit", tags=["Unit"])
app.include_router(LogController.router, prefix="/logs", tags=["Logs"])
app.include_router(ReportController.router, prefix="/report", tags=["Report"])
app.include_router(DialInController.router, prefix="/dialIn", tags=["DialIn"])
app.include_router(SupplierController.router, prefix="/supplier", tags=["Supplier"])
app.include_router(PipController.router, prefix="/pip", tags=["Pip"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
