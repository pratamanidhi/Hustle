from nicegui import ui

from HustleUserInterface.Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Business


business = Business()
class ModalElement:
    def __init__(self) -> None:
        pass

    def ShowModal(self, datas, type, userInfo):
        print(userInfo)
        if isinstance(datas, dict):
            datas = [datas]

        dialog = ui.dialog()

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name'},
            {'name': 'description', 'label': 'Description', 'field': 'description'},
        ]

        if userInfo['isAdmin']:
            columns.append({'name': 'stockIn', 'label': 'Stock In', 'field': 'stockIn'})

        columns += [
            {'name': 'stockOut', 'label': 'Stock Out', 'field': 'stockOut'},
            {'name': 'totalStock', 'label': 'Total Stock', 'field': 'totalStock'},
        ]

        rows = []
        for d in datas:
            row = {
                'name': str(d.get('name', '')),
                'description': str(d.get('description', '')),
                'stockOut': str(d.get('stockOut', '')),
                'totalStock': str(d.get('totalStock', '')),
            }
            if userInfo['isAdmin']:
                row['stockIn'] = str(d.get('stockIn'))
            rows.append(row)


        def onCheckout():
            datas[0]['updatedBy'] = userInfo['name']
            isOut = True
            item = {
                "type": type,
                "outQty": outQty.value,
                "isOut": isOut,
                "data" : datas
            }
            result = business.UpdateItem(item)
            if result:
                dialog.close()
            else:
                print(False)

        if userInfo['isAdmin']:
            def onCheckin():
                datas[0]['updatedBy'] = userInfo['name']
                isOut = False
                item = {
                    "type": type,
                    "inQty": inQty.value,
                    "isOut": isOut,
                    "data": datas
                }
                result = business.UpdateItem(item)
                if result:
                    dialog.close()
                else:
                    print(False)


        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):
            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            ui.label('Checkout Stock Item').classes('text-2xl font-semibold text-gray-800')

            ui.table(columns=columns, rows=rows, row_key='name').classes('w-full rounded border border-gray-300')
            ui.separator()
            with ui.column().classes('relative p-4 border rounded-md'):
                with ui.grid(columns=2).classes('gap-3'):
                    if userInfo['isAdmin']:
                        inQty = ui.input(label='Quantity Out') \
                            .props('type=number dense outlined') \
                            .classes('flex-1 text-sm').bind_visibility_from(userInfo['isAdmin'])
                        ui.button('Stock In', on_click=onCheckin) \
                            .classes('text-sm px-3 py-1 rounded-md')

                    outQty = ui.input(label='Quantity Out') \
                        .props('type=number dense outlined') \
                        .classes('flex-1 text-sm')
                    ui.button('Stock Out', on_click=onCheckout) \
                        .props('color=red dense') \
                        .classes('text-sm px-3 py-1 rounded-md')

        dialog.open()

    def ShowAddModal(self, type, userInfo):
        print(type)
        def onAddItem():
            value = {
                "type": type,
                "data": {
                    "name": name.value,
                    "stockIn": stockIn.value,
                    "packaging": packaging.value,
                    "price": itemPrice.value,
                    "description": description.value,
                    "unit": radio.value,
                    "updatedBy": userInfo['name']
                }
            }
            result = business.AddItem(value)
            if result:
                dialog.close()

        def getUnit():
            return business.GetUnit()

        dialog = ui.dialog()
        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):
            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')
            ui.label('Add new item').classes('text-2xl font-semibold text-gray-800')
            ui.separator()

            with ui.column().classes('relative p-4 border rounded-md'):
                with ui.grid(columns=2).classes('gap-3'):
                    ui.label('Product Name')
                    name = ui.input(label='Name') \
                        .props('dense outlined') \
                        .classes('w-60 text-sm')

                    ui.label('Product In')
                    stockIn = ui.input(label='Stock in') \
                        .props('type=number dense outlined') \
                        .classes('flex-1 text-sm')

                    ui.label('Product Packaging')
                    packaging = ui.input(label='Packaging') \
                        .props('type=number dense outlined') \
                        .classes('flex-1 text-sm')

                    unit_options = {u['guid']: u['name'] for u in getUnit()}
                    first_guid = next(iter(unit_options))
                    ui.label(f'Packaging Unit')
                    radio = ui.radio(unit_options, value=first_guid).props('inline')

                    ui.label('Product Price')
                    itemPrice = ui.input(label='Item price') \
                        .props('type=number dense outlined') \
                        .classes('flex-1 text-sm')

                    ui.label('Product Description')
                    description = ui.textarea(label='Description') \
                        .props('dense outlined') \
                        .classes('flex-1 text-sm')

            ui.button('Add product', on_click=onAddItem) \
                .classes('text-sm px-3 py-1 rounded-md')
        dialog.open()





