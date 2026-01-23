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
from HustleDatabase.Model.Logs.DailyStockReport import DailyStockReport as StockReport
from HustleDatabase.Repository.Pip.PipRepository import PipRepository as pipRepository
from HustleDatabase.Model.Pip.PipDeleteModel import PipDeleteModel

repo = Repo()
dbContext = DbContext()
dailyLog = DailyModel()
log = LogModel()
logBusiness = LogBusiness()
unit = Unit()
utils = Utils()
stockReport = StockReport()
pipRepo = pipRepository()

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
            Enum.Pip:(dbContext.Pip, Warehouse)
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

    def GetStockByGuid(self, database, guid):
        result = repo.GetStockByGuid(database, guid)
        return result

    def AddStock(self, types: Enum, model):
        if types in self.context_map:
            context, _ = self.context_map[types]
            return repo.AddStock(context, model)
        return "No Data"

    def UpdateStock(self, types: Enum, isOut, model):
        if types in self.context_map:
            context, _ = self.context_map[types]
            checkStock = repo.CheckStock(context, model)

            if checkStock["totalStock"] is None:
                checkStock["totalStock"] = 0

            if checkStock["stockIn"] is None:
                checkStock["stockIn"] = 0

            if checkStock["stockOut"] is None:
                checkStock["stockOut"] = 0

            if isOut:
                model.totalStock = float(checkStock["totalStock"]) - float(model.stockOut)
                model.stockOut =  float(model.stockOut)
                model.lastInput = checkStock["lastInput"]
                model.lastOutput = datetime.now()
            else:
                model.totalStock = float(checkStock["totalStock"]) + float(model.stockIn)
                model.stockIn = float(model.stockIn)
                model.lastInput = datetime.now()
                model.lastOutput = checkStock["lastOutput"]

            unitGuid = self.GetUnitGuid(model.unit)
            model.unit = unitGuid
            self.InsertLog(isOut, model)
            self.InsertIntoDaliyLog(model, isOut)
            self.InsertToDailyReport(types, model)
            return repo.StockUpdate(context, model)
        return "No Data"

    def DeleteStock(self, types:Enum, model):
        if types in self.context_map:
            context, _ = self.context_map[types]

            if(types == Ingredient.Pip):
                stockData = self.GetStockByGuid(context, model.guid)
                PipDeleteModel.name = stockData['name']
                pipRepo.DeletePip(PipDeleteModel)
            return repo.Delete(context, model)
        return False

    def DeletePipStock(self, name):
        try:
            context, _ = self.context_map[Ingredient.Pip]
            result = repo.DeletePipStock(context, name)
            return result
        except Exception as e:
            print(e)
            return False


    def GetUnitGuid(self, unitName):
        result = unit.GetUnitByName(unitName)
        return result["guid"]

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

    def InsertToDailyReport(self, types, model):
        if types in self.context_map:
            context, models = self.context_map[types]
            stockReport.name = model.name
            stockReport.category = context
            stockReport.stockOut = model.stockOut
            stockReport.stockIn = model.stockIn
            stockReport.totalStockTransaction = model.totalStock
            logBusiness.InputIntoDailyStockReport(stockReport)



    def InsertIntoDaliyLog(self, model, isOut):
        latestDatas = logBusiness.GetDailyLogByName(model.name)
        dailyLog.name = model.name
        dailyLog.price = model.price

        if latestDatas is not None:

            if isOut:
                if latestDatas["stockOut"] is None:
                    dailyLog.stockOut = int(model.stockOut)
                else:
                    dailyLog.stockOut = int(latestDatas["stockOut"]) + int(model.stockOut)

            else:
                if latestDatas["stockIn"] is None:
                    dailyLog.stockIn = int(model.stockIn)
                else:
                    dailyLog.stockIn = int(latestDatas["stockIn"]) + int(model.stockIn)

            result = logBusiness.UpdateDailyStock(model, isOut)
        else:

            if isOut:
                dailyLog.stockOut = int(model.stockOut)
            else:
                dailyLog.stockIn = int(model.stockIn)

            result = logBusiness.InsertDailyLog(dailyLog)
        return result