from nicegui import ui
from Common.Session.Session import Session as Session
from Common.Layout.Layout import Layout as Layout
from PIP.PipLayout import PipLayout as PipLayout
from Business.Warehouse.WarehouseBusiness import WarehouseBusiness as WarehouseBusiness
from Business.Common.CommonBusiness import CommonBusiness as CommonBusiness
warehouse = WarehouseBusiness()
common = CommonBusiness()


session = Session()
layout = Layout()
pipLayout = PipLayout()


def Content():
    @ui.page('/pip')
    def PipContent():
        with ui.row().classes('w-full h-screen items-center justify-center') as container:
            ui.label('Loading Data..')
            ui.spinner('dots', size='lg', color='red')

        async def Init():
            result = await session.Session()
            if result is not False:
                print("user: ", result)
                layout.Header(result)
                allStocks = warehouse.GetAllStock()
                ingredients = common.GetIngredient()
                units = common.GetUnit()

                pipLayout.PipContent(allStocks, ingredients, units, result['name'])
                container.visible = False
            else:
                ui.notify("No login info found", type='warning')
                ui.navigate.to('/')

        ui.timer(0.1, Init, once=True)