from HustleDatabase.ConnectionWarehouse import ConnectionWarehouse as Connection
import uuid
from datetime import datetime

db = Connection()

class SupplierRepository():
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self, dbContext):
        query = f"select * from {dbContext}"
        result = db.Execute(query)
        return result

    def InsertSupplier(self, dbContext, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = f"insert into {dbContext} (guid, name, orderType, bankNumber, bankName, contactPerson, updatedAt) values (?, ?, ?, ?, ?, ?, ?)"
        result = db.Execute(query, (
            guid,
            model.name,
            model.orderType,
            model.bankNumber,
            model.bankName,
            model.contactPerson,
            updatedAt
        ))
        return result

    def GetAllSupplierType(self, dbContext):
        query = f"select * from {dbContext}"
        result = db.Execute(query)
        return result

    def InsertSupplierType(self, dbContext, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = f"insert into {dbContext} (guid, name, updatedAt) values (?, ?, ?)"
        result = db.Execute(query, (
            guid,
            model.name,
            updatedAt
        ))
        return result

    def GetAllBankNumber(self, dbContext):
        query = f"select * from {dbContext}"
        result = db.Execute(query)
        return result

    def InputBankNumber(self, dbContext, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = f"insert into {dbContext} (guid, name, bankNumber, updatedAt) values (?, ?, ?, ?)"
        result = db.Execute(query, (
            guid,
            model.name,
            model.bankNumber,
            updatedAt
        ))
        return result