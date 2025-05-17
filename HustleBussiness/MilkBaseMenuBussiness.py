from HustleDatabase.Repository.MilkBaseModelRepo import MilkBaseRepo as MenuMilkBase

milkBase = MenuMilkBase()
class MilkBaseMenuBussiness():
    def __init__(self) -> None:
        pass

    def GetAllMilkBaseMenu(self):
        allMenus = milkBase.GetAllMilkBase()
        return allMenus