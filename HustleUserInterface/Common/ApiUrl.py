from HustleUserInterface.Common.ApiEnum import Enum as Enum

mainiUrl = 'http://localhost:8000'
class APIUrl:

    warehouse = mainiUrl + f"/{Enum.Warehouse}/get-stock"
    getAllWarehouse = mainiUrl + f"/{Enum.Warehouse}/get-all-stock"
    login = mainiUrl + f"/{Enum.UserManagement}/user-login"
    getAllUser = mainiUrl + f"/{Enum.UserManagement}/get-all-user"
    ingredientEnum = mainiUrl + f"/{Enum.Enum}/ingredient"
    ingredient = mainiUrl + f"/{Enum.Business}/ingredient"
    addStock = mainiUrl + f"/{Enum.Warehouse}/add-stock"
    checkOutStock = mainiUrl + f"/{Enum.Warehouse}/update-stock"
    deleteStock = mainiUrl + f"/{Enum.Warehouse}/delete"
    getAllUnit = mainiUrl + f"/{Enum.Unit}/get-unit"
    getUnitBytName = mainiUrl + f"/{Enum.Unit}/get-unit-by-name"
    insertLogs = mainiUrl + f"/{Enum.Log}/insert-log"
    getReport = mainiUrl + f"/{Enum.Report}/get-report"
    getAllReport = mainiUrl + f"/{Enum.Report}/get-report-all"
    getAllTools = mainiUrl + f"/{Enum.Warehouse}/get-tools"
    getAllDialIn = mainiUrl + f"/{Enum.DialIn}/get-all-dialIn"
    insertDialIn = mainiUrl + f"/{Enum.DialIn}/add-dialIn"
    getAllSupplier = mainiUrl + f"/{Enum.Supplier}/get-all-supplier"
    inputSupplier = mainiUrl + f"/{Enum.Supplier}/add-supplier"
