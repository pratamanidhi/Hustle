from Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Wh

wh = Wh()

type = 1
result = wh.GetAllStock()

for i in result:
    if i['type'] == type:
        print(i['data'])

