import json
from dataclasses import asdict

from HustleDatabase.Table.WarehouseTable import WarehouseTable as DbContext
from HustleCommon.Enums.Ingredient import Ingredient as Enum
from HustleDatabase.Repository.Warehouse.WarehouseRepository import WarehouseRepository as Repo
from HustleDatabase.Model.Warehouse.WarehouseModel import WarehouseModel as Warehouse
from datetime import datetime
from HustleBussiness.Log.LogBusiness import LogBusiness as LogBusiness
from HustleBussiness.Unit.UnitBusiness import UnitBusiness as Unit
from HustleDatabase.Model.Logs.DailyLogModel import DailyLogModel as DailyModel
from HustleDatabase.Model.Logs.LogModel import LogModel as LogModel
from HustleUtils.Utils import Utils as Utils
from HustleCommon.Enums.Ingredient import Ingredient as Ingredient

repo = Repo()
dbContext = DbContext()
dailyLog = DailyModel()
log = LogModel()
logBusiness = LogBusiness()
unit = Unit()
utils = Utils()

class WarehouseBusiness:
    def __init__(self) -> None:
        self.context_map = {
            Enum.Coffee: (dbContext.Coffee, Warehouse),
            Enum.Juice: (dbContext.Juice, Warehouse),
            Enum.MilkAndCream: (dbContext.MilkAndCream, Warehouse),
            Enum.Other: (dbContext.Other, Warehouse),
            Enum.Powder: (dbContext.Powder, Warehouse),
            Enum.Syrup: (dbContext.Syrup, Warehouse),
            Enum.Tea: (dbContext.Tea, Warehouse),
            Enum.Topping: (dbContext.Topping, Warehouse),
        }

    def GetAllStock(self):
        datas = []
        for i in Ingredient:
            if i in self.context_map:
                context, model = self.context_map[i]
                result = repo.GetStock(context, model)

                data = {
                    'type': i,
                    'data': result
                }
                datas.append(data)
        return datas

    def GetStock(self, types: Enum):
        if types in self.context_map:
            context, model = self.context_map[types]
            return repo.GetStock(context, model)
        return "No Data"

    def AddStock(self, types: Enum, model):
        if types in self.context_map:
            context, _ = self.context_map[types]

            return repo.AddStock(context, model)
        return "No Data"

    def UpdateStock(self, types: Enum, isOut, model):
        if types in self.context_map:
            context, _ = self.context_map[types]
            checkStock = repo.CheckStock(context, model)

            if isOut:
                model.totalStock = int(checkStock['totalStock']) - model.stockOut
                model.stockOut =  model.stockOut
                model.lastInput = checkStock['lastInput']
                model.lastOutput = datetime.now()
            else:
                model.totalStock = int(checkStock['totalStock']) + model.stockIn
                model.stockIn = model.stockIn
                model.lastInput = datetime.now()
                model.lastOutput = checkStock['lastOutput']

            unitGuid = self.GetUnitGuid(model.unit)
            model.unit = unitGuid
            self.InsertLog(isOut, model)
            self.InsertIntoDaliyLog(model, isOut)
            return repo.StockUpdate(context, model)
        return "No Data"

    def DeleteStock(self, types:Enum, model):
        if types in self.context_map:
            context, _ = self.context_map[types]
            return repo.Delete(context, model)
        return False


    def GetUnitGuid(self, unitName):
        result = unit.GetUnitByName(unitName)
        return result['guid']

    def InsertLog(self, isOut, data):
        data.lastInput = utils.FormatedDate(data.lastInput)
        data.lastOutput = utils.FormatedDate(data.lastOutput)
        action = {
            "data": {
                "isOut": isOut,
                "input": json.dumps(data.dict())
            }
        }
        log.user = data.updatedBy
        log.action = str(action)

        result = logBusiness.InsertLog(log)
        return result


    def InsertIntoDaliyLog(self, model, isOut):
        print(model)
        latestDatas = logBusiness.GetDailyLogByName(model.name)
        print(f"latest: {latestDatas}")
        dailyLog.name = model.name
        dailyLog.price = model.price

        if latestDatas is not None:

            if isOut:
                if latestDatas['stockOut'] is None:
                    dailyLog.stockOut = int(model.stockOut)
                else:
                    dailyLog.stockOut = int(latestDatas['stockOut']) + int(model.stockOut)

            else:
                if latestDatas['stockIn'] is None:
                    dailyLog.stockIn = int(model.stockIn)
                else:
                    dailyLog.stockIn = int(latestDatas['stockIn']) + int(model.stockIn)

            result = logBusiness.UpdateDailyStock(model, isOut)
        else:

            if isOut:
                dailyLog.stockOut = int(model.stockOut)
            else:
                dailyLog.stockIn = int(model.stockIn)

            result = logBusiness.InsertDailyLog(dailyLog)
        return result