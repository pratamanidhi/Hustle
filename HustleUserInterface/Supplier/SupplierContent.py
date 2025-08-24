from nicegui import ui
from Common.Session.Session import Session as Session
from Common.Layout.Layout import Layout as Layout
from Supplier.SupplierLayout import SupplierLayout as SupplierLayout
from Business.Supplier.SupplierBusiness import SupplierBusiness as SupplierBusiness

session = Session()
layout = Layout()
supplierBusiness = SupplierBusiness()

supplierLayout = SupplierLayout()

def SupplierList(user):
    result = supplierBusiness.GetAllSupplier()
    supplierLayout.SupplierContent(result, user)

@ui.page('/supplier')
def SupplierContent():
    with ui.row().classes('w-full h-screen items-center justify-center') as container:
        ui.label('Loading Data..')
        ui.spinner('dots', size='lg', color='red')

    async def Init():
        result = await session.Session()
        if result is not False:
            print("user: ", result)
            layout.Header(result)
            SupplierList(result)
            container.visible = False
        else:
            ui.notify("No login info found", type='warning')
            ui.navigate.to('/')

    ui.timer(0.1, Init, once=True)
