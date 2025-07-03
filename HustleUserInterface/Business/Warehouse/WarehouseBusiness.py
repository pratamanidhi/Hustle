from HustleUserInterface.API.Warehouse.WarehouseAPI import WarehouseAPI as Warehouse
from HustleUserInterface.Business.Logs.LogsBusiness import LogsBusiness as Log
from HustleUserInterface.API.Unit.UnitAPI import UnitAPI as Unit
from Common.StockEnum import StockEnum as Enum
from Common.StockName import  StockName as StockName
from datetime import datetime


warehouse = Warehouse()
log = Log()
unit = Unit()
stockName = StockName()
class WarehouseBusiness:
    def __init__(self) -> None:
        self.context_map = {
            Enum.Coffee: stockName.Coffee,
            Enum.Juice: stockName.Juice,
            Enum.MilkAndCream: stockName.MilkAndCream,
            Enum.Other: stockName.Other,
            Enum.Powder: stockName.Powder,
            Enum.Syrup: stockName.Syrup,
            Enum.Tea: stockName.Tea,
            Enum.Topping: stockName.Topping
        }
        pass

    def GetStock(self, type):
        rows = warehouse.GetStock(type)
        newRow = []
        for row in rows:
            rowCopy = row.copy()
            if rowCopy.get('lastInput'):
                try:
                    dt_object = datetime.fromisoformat(rowCopy['lastInput'])
                    rowCopy['lastInput'] = dt_object.strftime('%Y-%b-%d %H:%M:%S')
                except ValueError:
                    rowCopy['lastInput'] = 'Invalid Date'
            else:
                rowCopy['lastInput'] = '-'

            if rowCopy.get('lastOutput'):
                try:
                    dt_object = datetime.fromisoformat(rowCopy['lastOutput'])
                    rowCopy['lastOutput'] = dt_object.strftime('%Y-%b-%d %H:%M:%S')
                except ValueError:
                    rowCopy['lastOutput'] = 'Invalid Date'
            else:
                rowCopy['lastOutput'] = '-'

            if rowCopy.get('price') is not None:
                try:
                    price_value = int(rowCopy['price'])
                    formatted_price = f"Rp {price_value:,.0f}".replace(",", ".")
                    rowCopy['price'] = formatted_price
                except (ValueError, TypeError):
                    rowCopy['price'] = 'N/A'
            else:
                rowCopy['price'] = '-'

            if rowCopy.get('priceUnit') is not None:
                try:
                    price_value = int(rowCopy['priceUnit'])
                    formatted_price = f"Rp {price_value:,.0f}".replace(",", ".")
                    rowCopy['priceUnit'] = formatted_price
                except (ValueError, TypeError):
                    rowCopy['priceUnit'] = 'N/A'
            else:
                rowCopy['price'] = '-'

            newRow.append(rowCopy)

        return newRow

    def GetAllStock(self):
        datas = warehouse.GetAllStock()
        newDatas = []
        for rows in datas:
            newRow = []
            for row in rows['data']:
                rowCopy = row.copy()
                if rowCopy.get('lastInput'):
                    try:
                        dt_object = datetime.fromisoformat(rowCopy['lastInput'])
                        rowCopy['lastInput'] = dt_object.strftime('%Y-%b-%d %H:%M:%S')
                    except ValueError:
                        rowCopy['lastInput'] = 'Invalid Date'
                else:
                    rowCopy['lastInput'] = '-'

                if rowCopy.get('lastOutput'):
                    try:
                        dt_object = datetime.fromisoformat(rowCopy['lastOutput'])
                        rowCopy['lastOutput'] = dt_object.strftime('%Y-%b-%d %H:%M:%S')
                    except ValueError:
                        rowCopy['lastOutput'] = 'Invalid Date'
                else:
                    rowCopy['lastOutput'] = '-'

                if rowCopy.get('price') is not None:
                    try:
                        price_value = int(rowCopy['price'])
                        formatted_price = f"Rp {price_value:,.0f}".replace(",", ".")
                        rowCopy['price'] = formatted_price
                    except (ValueError, TypeError):
                        rowCopy['price'] = 'N/A'
                else:
                    rowCopy['price'] = '-'

                if rowCopy.get('priceUnit') is not None:
                    try:
                        price_value = int(rowCopy['priceUnit'])
                        formatted_price = f"Rp {price_value:,.0f}".replace(",", ".")
                        rowCopy['priceUnit'] = formatted_price
                    except (ValueError, TypeError):
                        rowCopy['priceUnit'] = 'N/A'
                else:
                    rowCopy['price'] = '-'

                newRow.append(rowCopy)

            if rows['type'] in self.context_map:
                type = self.context_map[rows['type']]
                newDataOfStock = {
                    'name' : type,
                    'type' : rows['type'],
                    'data' : newRow
                }
                newDatas.append(newDataOfStock)

        print(newDatas)
        return newDatas



    def AddItem(self, item):
        item['data']['stockIn'] = int(item['data']['stockIn'])
        item['data']['packaging'] = int(item['data']['packaging'])
        item['data']['price'] = int(item['data']['price'])
        return warehouse.AddStock(item)

    def UpdateItem(self, item):
        print(item)

        data = item["data"][0]

        if item['inPrice'] is not None:
            data['price'] = item['itemPrice']
        else:
            data["price"] = int(data["price"].replace('Rp', '').replace('.', '').strip())

        data["priceUnit"] = int(data["priceUnit"].replace('Rp', '').replace('.', '').strip())
        data["lastInput"] = None
        data["lastOutput"] = None
        if item['isOut']:
            data["stockOut"] = int(item["outQty"])
        else:
            data["stockIn"] = int(item['inQty'])
        result = warehouse.CheckOutStock(item["type"], item["isOut"], data)
        return result

    def GetUnit(self):
        return unit.GetAllUnit()

    def DeleteStock(self, item):
        data = item['data'][0]
        return warehouse.DeleteStock(item['type'], data['guid'])






