from charset_normalizer.cli import query_yes_no

from HustleUserInterface.API.Supplier.SupplierAPI import SupplierAPI as Api

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

    def ReceiveOrder(self, supplierId, quantity):
        if supplierId is not None and quantity is not None:
            jsons = {
                "supplierId" : supplierId,
                "quantity": quantity
            }
            return api.ReceiveOrder(jsons)
        else:
            return False