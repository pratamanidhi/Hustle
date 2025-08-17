from nicegui import ui
from datetime import datetime
from Supplier.SupplierModal import SupplierModal as Modal

modal = Modal()
class SupplierLayout:
    def __init__(self) -> None:
        pass

    def SupplierContent(self, supplierList, user):
        def addNewSupplier():
            modal.AddSupplierModal()

        content_container = ui.column().classes('w-full h-full')
        with content_container:
            with ui.splitter(value=10).classes('w-full h-full') as splitter:
                with splitter.before:
                    with ui.tabs().props('vertical').classes('w-50') as tabs:
                        list_tab = ui.tab('Supplier List')
                        history_tab = ui.tab('Supplier History')

                with splitter.after:
                    with ui.tab_panels(tabs, value=list_tab).props('vertical').classes('w-full h-full'):
                        with ui.tab_panel(list_tab):
                            with ui.grid(columns=2).classes('gap-5'):
                                ui.button('Add new supplier', on_click=addNewSupplier) \
                                    .props('flat dense')

                            ui.separator()
                            ui.label("List of supplier").classes('font-semibold text-gray-800')
                            with ui.grid().classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 w-full'):
                                for supplier in supplierList:
                                    with ui.card().classes('p-0 shadow-sm !border-0 w-full'):
                                        self.SupplierListContent(supplier, user)
                        with ui.tab_panel(history_tab):
                            ui.label('Supplier history list')

    def SupplierListContent(self, supplier, user):
        def onDeleteItem():
            modal.ConfirmationDeleteModal(supplier)

        def receiveOrder():
            modal.ReceiveOrderModal(supplier, user)


        with ui.column().classes('w-full relative p-4 border-2 rounded-3xl'):
            ui.button("Receive", on_click=receiveOrder) \
                .props('flat round dense color=black') \
                .classes('absolute top-2 right-10 z-10')


            dates = datetime.now()
            newDate = dates.strftime("%d %b %Y %H:%M")
            ui.chip(icon='calendar_today', color='indigo-5', removable=False).style(
                'color: white; padding-left: 8px; gap: 0.5rem').set_text(newDate)
            with ui.column().classes('w-full p-4 border-2 rounded-3xl h-full'):
                with ui.grid(columns=2).classes('gap-5'):
                    ui.label("Supplier Name").classes('font-semibold text-gray-800')
                    ui.label(supplier['name'])

                    ui.label("Product Name").classes('font-semibold text-gray-800')
                    ui.label(supplier['productName'])

                    ui.label("Product Category").classes('font-semibold text-gray-800')
                    ui.label(supplier['orderType'])

                    ui.label("Bank Name").classes('font-semibold text-gray-800')
                    ui.label(supplier['bankName'])

                    ui.label("Bank Number").classes('font-semibold text-gray-800')
                    ui.label(supplier['bankNumber'])

                    ui.label("Contact Person").classes('font-semibold text-gray-800')
                    ui.label(supplier['contactPerson'])

            ui.button('Delete', on_click=onDeleteItem) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')
