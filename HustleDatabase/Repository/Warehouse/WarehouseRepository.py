from HustleDatabase.ConnectionWarehouse import ConnectionWarehouse as Connection
from datetime import datetime
import uuid

class WarehouseRepository():
    def __init__(self) -> None:
        pass

    def GetStock(self, table, model):
        db = Connection()
        query = f'select A.guid, A.name, A.description, A.stockIn, A.stockOut, A.totalStock, A.lastInput, A.lastOutput, A.updatedBy, A.price, B.name as unit, A.packaging, A.priceUnit from {table} AS A INNER JOIN Unit AS B WHERE A.unit = B.guid'
        stock = db.Execute( query, model)
        return stock

    def AddStock(self, table, model):
        db = Connection()
        guid = str(uuid.uuid4())
        priceUnit = model.price/model.packaging
        query = f'INSERT INTO {table} (guid, name, description, stockIn, stockOut, totalStock, lastInput, lastOutput, updatedBy, price, unit, packaging, priceUnit) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
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
                             model.price,
                             model.unit,
                             model.packaging,
                             priceUnit))
        return result

    def GetIngredient(self, table, model):
        db = Connection()
        query = f'Select guid, name, priceUnit from {table}'
        ingredient = db.Execute(query, model)
        return ingredient

    def StockUpdate(self, table, isOut, model):
        db = Connection()
        query = f'SELECT * FROM {table} WHERE guid = ? AND name = ?'
        result = db.Execute(query,
                            (model.guid,
                             model.name))
        checkStock =  dict(result[0])

        if isOut:
            totalStock = int(checkStock['totalStock']) - model.stockOut
            stockIn = checkStock['stockIn']
            stockOut = int(checkStock['stockOut']) + model.stockOut
            lastInput = checkStock['lastInput']
            lastOutput = datetime.now()
        else:
            totalStock = int(checkStock['totalStock']) + model.stockIn
            stockIn = model.stockIn
            stockOut = checkStock['stockOut']
            lastInput = datetime.now()
            lastOutput = checkStock['lastOutput']

        query = f'''UPDATE {table}
                   SET guid = ?, name = ?, description = ?, stockIn = ?, stockOut = ?, totalStock = ?, lastInput = ?, lastOutput = ?, updatedBy = ?, price = ?, unit = ?, packaging = ?, priceUnit = ?
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
                checkStock['unit'],
                checkStock['packaging'],
                checkStock['priceUnit'],
                checkStock['guid'],
                checkStock['name']
            ))
            return result
        except Exception as e:
            print("Error updating stock:", str(e))
            return False
