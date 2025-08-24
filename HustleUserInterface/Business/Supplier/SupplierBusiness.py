
from API.Supplier.SupplierAPI import SupplierAPI as Api

api = Api()
class SupplierBusiness:
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self):
        return api.GetAllSupplier()

    def GetAllSupplierCategory(self):
        return api.GetAllSupplierCategory()

    def InputSupplier(self, input):
        return api.InputSupplier(input)

    def GetSupplierByCategory(self, body):
        if body is not None:
            jsons = {
                "name" : body
            }
            return api.GetSupplierByCategory(jsons)
        else:
            return False

    def ReceiveOrder(self, supplierId, quantity, receivedBy):
        if supplierId is not None and quantity is not None:
            jsons = {
                "supplierId" : supplierId,
                "quantity": quantity,
                "receiveBy": receivedBy["name"]
            }
            return api.ReceiveOrder(jsons)
        else:
            return False

    def DeleteSupplier(self, guid):
        if guid is not None:
            jsons = {
                "guid": guid
            }
            return api.DeleteSupplier(jsons)
        else:
            return False
