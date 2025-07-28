from nicegui import ui
from datetime import datetime
from HustleUserInterface.Business.Supplier.SupplierBusiness import SupplierBusiness as Business

business = Business()
class SupplierModal():
    def __init__(self) -> None:
        pass

    def AddSupplierModal(self):

        dialog = ui.dialog()

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):

            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            ui.label('Supplier Form').classes('text-2xl font-semibold text-gray-800')
            dateNow = datetime.now().strftime("%d %b %Y %H:%M")
            ui.chip( color='amber-500', removable=False).style(
                'color: white; padding-left: 8px; gap: 0.5rem').set_text(dateNow)
            ui.separator()

            with ui.column().classes('relative p-4 border rounded-md'):
                with ui.grid(columns=2).classes('gap-3'):
                    ui.label('Supplier Name')
                    name = ui.input(label='Name') \
                        .props('dense outlined') \
                        .classes('w-60 text-sm')

                    ui.label('Product')
                    product = ui.input(label='Product') \
                        .props('dense outlined') \
                        .classes('w-60 text-sm')

                    ui.label('Bank Name')
                    bankName = ui.input(label='Bank Name') \
                        .props('dense outlined') \
                        .classes('w-60 text-sm')

                    ui.label('Bank Number')
                    bankNumber = ui.input(label='Bank Number') \
                        .props('type=number dense outlined') \
                        .classes('w-60 text-sm')

                    ui.label('Contact Person')
                    contactPerson = ui.input(label='Contact Person') \
                        .props('type=number dense outlined') \
                        .classes('w-60 text-sm')

            def onAddSupplier():
                datas = {
                    "name" : name.value,
                    "orderType" : product.value,
                    "bankName" : bankName.value,
                    "bankNumber" : bankNumber.value,
                    "contactPerson": contactPerson.value
                }

                result = business.InputSupplier(datas)
                if result:
                    ui.notify("Success to add new supplier")
                    ui.navigate.to('/supplier')
                    dialog.close()
                else:
                    ui.notify("Failed to add new supplier")

            ui.button('Add product', on_click=onAddSupplier) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

        dialog.open()