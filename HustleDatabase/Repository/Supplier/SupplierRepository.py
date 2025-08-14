from HustleDatabase.ConnectionWarehouse import ConnectionWarehouse as Connection
import uuid
from datetime import datetime

db = Connection()

class SupplierRepository():
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self, dbContext):
        query = f"""
            SELECT 
                s.guid, 
                s.name, 
                s.contactPerson, 
                s.productName,
                s.updatedAt, 
                ot.name AS orderType, 
                ba.name AS bankName, 
                ba.bankNumber 
            FROM {dbContext} AS s
            JOIN OrderType AS ot ON s.orderType = ot.guid
            JOIN BankAccount AS ba ON s.bankAccount = ba.guid
        """
        result = db.Execute(query)
        return result

    def GetSupplierWithCategory(self, dbContext, orderType):
        query = f"""
            SELECT 
                    s.guid, 
                    s.name, 
                    s.contactPerson, 
                    s.productName,
                    s.updatedAt, 
                    ot.name AS orderType, 
                    ba.name AS bankName, 
                    ba.bankNumber 
                FROM {dbContext} AS s
                JOIN OrderType AS ot ON s.orderType = ot.guid
                JOIN BankAccount AS ba ON s.bankAccount = ba.guid
                where orderType = ?
        """
        result = db.Execute(query, (orderType,))
        return result

    def InsertSupplier(self, dbContext, model):
        print("model", model)
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = f"insert into {dbContext} (guid, name, orderType, productName, bankAccount, contactPerson, updatedAt) values (?, ?, ?, ?, ?, ?, ?)"
        result = db.Execute(query, (
            guid,
            model.name,
            model.orderType,
            model.productName,
            model.bankAccount,
            model.contactPerson,
            updatedAt
        ))
        return result

    def GetAllSupplierType(self, dbContext):
        query = f"select * from {dbContext}"
        result = db.Execute(query)
        return result

    def GetSupplierId(self, dbContext, input):
        query = f"select guid from {dbContext} where name = ?"
        result = db.Execute(query, (input.name,))
        if result:
            return dict(result[0])
        else:
            return None

    def InsertSupplierType(self, dbContext, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = f"insert into {dbContext} (guid, name, updatedAt) values (?, ?, ?)"
        db.Execute(query, (
            guid,
            model.name,
            updatedAt
        ))

        data = self.GetSupplierId(dbContext, model.name)
        return data

    def GetAllBankNumber(self, dbContext):
        query = f"select * from {dbContext}"
        result = db.Execute(query)
        return result

    def GetBankNumberId(self, dbContext, input):
        print(input)
        query = f'select guid from {dbContext} where name = ? and bankNumber = ?'
        result = db.Execute(query, (input.bankName, input.bankNumber))
        if result:
            return dict(result[0])
        else:
            return None


    def InputBankNumber(self, dbContext, model):
        guid = str(uuid.uuid4())
        updatedAt = datetime.now()
        query = f"insert into {dbContext} (guid, name, bankNumber, updatedAt) values (?, ?, ?, ?)"
        db.Execute(query, (
            guid,
            model.bankName,
            model.bankNumber,
            updatedAt
        ))
        data = self.GetBankNumberId(dbContext, model)
        return data