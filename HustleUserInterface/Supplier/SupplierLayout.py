from nicegui import ui
from datetime import datetime
from typing import Dict

from Business.Supplier.SupplierBusiness import SupplierBusiness as SupplierBusiness
from Supplier.SupplierModal import SupplierModal as Modal

modal = Modal()
supplierBusiness = SupplierBusiness()
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
                            self.GetSupplierHistory()

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
                    ui.label(supplier["name"])

                    ui.label("Product Name").classes('font-semibold text-gray-800')
                    ui.label(supplier["productName"])

                    ui.label("Product Category").classes('font-semibold text-gray-800')
                    ui.label(supplier["orderType"])

                    ui.label("Bank Name").classes('font-semibold text-gray-800')
                    ui.label(supplier["bankName"])

                    ui.label("Bank Number").classes('font-semibold text-gray-800')
                    ui.label(supplier["bankNumber"])

                    ui.label("Contact Person").classes('font-semibold text-gray-800')
                    ui.label(supplier["contactPerson"])

            ui.button('Delete', on_click=onDeleteItem) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

    def GetSupplierHistory(self):
        result = supplierBusiness.GetSupplierHistory()
        if result is not False:
            print(result)

            columns = [
                {'no': 'no', 'label': 'No', 'field': 'no', 'required': True, 'align': 'left'},
                {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
                {'name': 'productType', 'label': 'Product Type', 'field': 'productType', 'sortable': True,
                 'align': 'left'},
                {'name': 'productName', 'label': 'Product Name', 'field': 'productName', 'sortable': True,
                 'align': 'left'},
                {'name': 'bankAccount', 'label': 'Bank Account', 'field': 'bankAccount', 'sortable': True,
                 'align': 'left'},
                {'name': 'bankNumber', 'label': 'Bank Number', 'field': 'bankNumber', 'sortable': True,
                 'align': 'left'},
                {'name': 'contactPerson', 'label': 'Contact Person', 'field': 'contactPerson', 'sortable': True,
                 'align': 'left'},
                {'name': 'quantity', 'label': 'Quantity', 'field': 'quantity', 'sortable': True, 'align': 'left'},
                {'name': 'receivedBy', 'label': 'Received By', 'field': 'receivedBy', 'sortable': True,
                 'align': 'left'},
                {'name': 'dateReceived', 'label': 'Date Received', 'field': 'dateReceived', 'sortable': True,
                 'align': 'left'},
            ]
            rows = result

            def toggle(column: dict, visible: bool) -> None:
                column['classes'] = '' if visible else 'hidden'
                column['headerClasses'] = '' if visible else 'hidden'
                table.update()

            with ui.button(icon='menu'):
                with ui.menu(), ui.column().classes('gap-0 p-2'):
                    for column in columns:
                        ui.switch(column['label'], value=True,
                                  on_change=lambda e, column=column: toggle(column, e.value))

            table = ui.table(columns=columns, rows=rows, row_key='name')
            table.add_slot('body-cell-dateReceived', '''
              <q-td key="dateReceived" :props="props">
                <q-chip color="indigo-5" text-color="white" dense>
                  {{ props.value }}
                </q-chip>
              </q-td>
            ''')
            table.add_slot('body-cell-quantity', '''
              <q-td key="quantity" :props="props">
                <q-chip :color="props.value <= 5 ? 'red' : 'green'" text-color="white" dense>
                  {{ props.value }}
                </q-chip>
              </q-td>
            ''')



