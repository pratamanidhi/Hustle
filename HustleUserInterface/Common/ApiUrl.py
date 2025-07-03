from HustleUserInterface.Common.ApiEnum import Enum as Enum

mainiUrl = 'http://localhost:8000'
class APIUrl:

    warehouse = mainiUrl + f"/{Enum.Warehouse}/get-stock"
    getAllWarehouse = mainiUrl + f"/{Enum.Warehouse}/get-all-stock"
    login = mainiUrl + f"/{Enum.UserManagement}/user-login"
    ingredientEnum = mainiUrl + f"/{Enum.Enum}/ingredient"
    ingredient = mainiUrl + f"/{Enum.Business}/ingredient"
    addStock = mainiUrl + f"/{Enum.Warehouse}/add-stock"
    checkOutStock = mainiUrl + f"/{Enum.Warehouse}/update-stock"
    deleteStock = mainiUrl + f"/{Enum.Warehouse}/delete"
    getAllUnit = mainiUrl + f"/{Enum.Unit}/get-unit"
    getUnitBytName = mainiUrl + f"/{Enum.Unit}/get-unit-by-name"
    insertLogs = mainiUrl + f"/{Enum.Log}/insert-log"
