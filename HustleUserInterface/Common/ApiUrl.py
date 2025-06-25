from HustleUserInterface.Common.ApiEnum import Enum as Enum

mainiUrl = 'http://localhost:8000'
class APIUrl:

    warehouse = mainiUrl + f"/{Enum.Warehouse}/get-stock"
    login = mainiUrl + f"/{Enum.UserManagement}/user-login"
    ingredientEnum = mainiUrl + f"/{Enum.Enum}/ingredient"
    ingredient = mainiUrl + f"/{Enum.Business}/ingredient"
    addStock = mainiUrl + f"/{Enum.Warehouse}/add-stock"
    checkOutStock = mainiUrl + f"/{Enum.Warehouse}/update-stock"
    getAllUnit = mainiUrl + f"/{Enum.Unit}/get-unit"
    getUnitBytName = mainiUrl + f"/{Enum.Unit}/get-unit-by-name"
