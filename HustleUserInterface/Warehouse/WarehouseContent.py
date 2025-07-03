from nicegui import ui
from HustleUserInterface.Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Warehouse
from HustleUserInterface.Common.Button import Button as Button
from Common.Layout.Layout import Layout as Layout
from Common.Session.Session import Session as Session

warehouse = Warehouse()
button = Button()
layout = Layout()
session = Session()

@ui.page('/warehouse')
def WarehouseContent():
    with ui.row().classes('w-full h-screen items-center justify-center') as container:
        ui.label('Loading Data..')
        ui.spinner('dots', size='lg', color='red')

    async def init():
        result = await session.Session()
        if result is not False:
            layout.Header(result)

            with ui.row().classes('w-full justify-evenly'):
                allStock = warehouse.GetAllStock()
                for stock in allStock:
                    layout.RenderTable(stock['type'], stock['name'], result, stock['data'])

            container.visible = False
        else:
            ui.notify("No login info found", type='warning')
            ui.navigate.to('/')

    ui.timer(0.1, init, once=True)




