from nicegui import ui
from Common.Session.Session import Session as Session
from Common.Layout.Layout import Layout as Layout
from Common.Modal.ModalElement import ModalElement as Modal
from Business.Warehouse.WarehouseBusiness import WarehouseBusiness as WarehouseBusiness
from Business.Common.CommonBusiness import CommonBusiness as CommonBusiness
from Menu.MenuLayout import MenuLayout as MenuLayout

session = Session()
layout = Layout()
modal = Modal()
warehouse = WarehouseBusiness()
common = CommonBusiness()
menuLayout = MenuLayout()

def GenerateContent(stocks, ingredients, units):

    def CreateMenuItem():
        modal.ShowAddMenuModal(stocks, ingredients, units)


    ui.button('Add new', on_click=CreateMenuItem) \
        .props('flat dense')
    menuLayout.ShowMenu()

def Content():
    @ui.page('/menu')
    def MenuContent():
        with ui.row().classes('w-full h-screen items-center justify-center') as container:
            ui.label('Loading Data..')
            ui.spinner('dots', size='lg', color='red')

        async def Init():
            result = await session.Session()
            if result is not False:
                allStocks = warehouse.GetAllStock()
                ingredients = common.GetIngredient()
                units = common.GetUnit()
                layout.Header(result)
                container.visible = False
                GenerateContent(allStocks, ingredients, units)
            else:
                ui.notify("No login info found", type='warning')
                ui.navigate.to('/')

        ui.timer(0.1, Init, once=True)