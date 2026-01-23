from HustleDatabase.Model.Menu.MenuModel import MenuModel as menuModel
from HustleDatabase.Repository.Menu.MenuRepository import MenuRepository as Repository


repo = Repository()

class MenuBusiness():
    def __init__(self) -> None:
        pass

    def InputMenu(self, input):
        try:
            menuModel.name = input.name
            menuModel.ingredient = input.ingredient
            menuModel.price = input.price
            menuModel.category = input.category
            result = repo.InputMenu(menuModel)
            return result
        except Exception as e:
            return e