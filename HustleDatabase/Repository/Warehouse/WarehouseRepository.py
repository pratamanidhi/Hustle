from HustleDatabase.ConnectionWarehouse import ConnectionWarehouse as Connection
from datetime import datetime
import uuid

class WarehouseRepository():
    def __init__(self) -> None:
        pass

    def GetStock(self, table, model):
        db = Connection()
        query = f'SELECT * FROM {table}'
        stock = db.Execute( query, model)
        return stock

    def AddStock(self, table, model):
        db = Connection()
        guid = str(uuid.uuid4())
        query = f'INSERT INTO {table} (guid, name, description, stockIn, stockOut, totalStock, lastInput, lastOutput, updatedBy, price) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        result = db.Execute(query,
                            (guid,
                             model.name,
                             model.description,
                             model.stockIn,
                             model.stockOut,
                             model.totalStock,
                             datetime.now(),
                             None,
                             model.updatedBy,
                             model.price))
        return result

    def CheckStock(self, table, model):
        db = Connection()
        query = f'SELECT * FROM {table} WHERE guid = ? AND name = ?'
        result = db.Execute(query,
                            (model.guid,
                             model.name))
        return dict(result[0])

    def StockUpdate(self, table, isOut, model):
        db = Connection()
        checkStock = self.CheckStock(model)

        if isOut:
            totalStock = int(checkStock['totalStock']) - model.stockOut
            stockIn = checkStock['stockIn']
            stockOut = model.stockOut
            lastInput = checkStock['lastInput']
            lastOutput = datetime.now()
        else:
            totalStock = int(checkStock['totalStock']) + model.stockIn
            stockIn = model.stockIn
            stockOut = checkStock['stockOut']
            lastInput = datetime.now()
            lastOutput = checkStock['lastOutput']

        query = f'''UPDATE {table}
                   SET guid = ?, name = ?, description = ?, stockIn = ?, stockOut = ?, 
                       totalStock = ?, lastInput = ?, c = ?, updatedBy = ?, price = ?
                   WHERE guid = ? AND name = ?'''

        try:
            result = db.Execute(query, (
                checkStock['guid'],
                checkStock['name'],
                checkStock['description'],
                stockIn,
                stockOut,
                totalStock,
                lastInput,
                lastOutput,
                model.updatedBy,
                checkStock['price'],
                checkStock['guid'],  # for WHERE clause
                checkStock['name']  # for WHERE clause
            ))
            return result
        except Exception as e:
            print("Error updating stock:", str(e))
            return False
