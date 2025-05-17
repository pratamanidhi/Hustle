from HustleDatabase.Repository.MenuCoffeeRepo import MenuCoffeeRepo as MenuCoffee


Coffee = MenuCoffee()
class CoffeeMenuBussiness():

    def __init__(self) -> None:
        pass

    def GetAllCoffeeMenus(self):
        allMenus = Coffee.GetAllCoffee()
        return allMenus

    def CreateCoffeeMenu(self, coffee):
        createMenu = Coffee.AddCoffee(coffee)
        return createMenu
