from HustleUserInterface.API.Supplier.SupplierAPI import SupplierAPI as Api

api = Api()
class SupplierBusiness:
    def __init__(self) -> None:
        pass

    def GetAllSupplier(self):
        return api.GetAllSupplier()

    def InputSupplier(self, input):
        return api.InputSupplier(input)