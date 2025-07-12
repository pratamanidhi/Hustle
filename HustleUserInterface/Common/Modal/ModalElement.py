from nicegui import ui
from nicegui.elements.button_dropdown import DropdownButton

from HustleUserInterface.Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Business
from Business.Common.CommonBusiness import CommonBusiness as CommonBusiness

business = Business()
commonBusiness = CommonBusiness()

class ModalElement:
    def __init__(self) -> None:
        pass

    def ShowModal(self, datas, type, userInfo):
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
                "data": datas
            }
            result = business.UpdateItem(item)
            if result:
                dialog.close()
                ui.navigate.to('/warehouse')
            else:
                print(False)

        if userInfo['isAdmin']:
            def onCheckin():
                datas[0]['updatedBy'] = userInfo['name']
                isOut = False
                item = {
                    "type": type,
                    "inQty": inQty.value,
                    ""
                    "isOut": isOut,
                    "data": datas
                }
                result = business.UpdateItem(item)
                if result:
                    dialog.close()
                    ui.navigate.to('/warehouse')
                else:
                    print(False)

            def onDeleteItem():
                item = {
                    "type": type,
                    "data": datas
                }
                result = business.DeleteStock(item)
                if result:
                    dialog.close()
                    ui.navigate.to('/warehouse')
                else:
                    print(False)

            def onUpdatePrice():
                datas[0]['updatedBy'] = userInfo['name']
                isOut = False
                item = {
                    'type': type,
                    'inQty': inQty.value,
                    'inPrice': inPrice.value,
                    'isOut': isOut,
                    'data': datas
                }
                result = business.UpdateItem(item)
                if result:
                    dialog.close()
                    ui.navigate.to('/warehouse')
                else:
                    print(False)
                return

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):
            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            if userInfo['isAdmin']:
                ui.label('Manage Stock').classes('text-2xl font-semibold text-gray-800')
            else:
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

                        formatedPrice = int(datas[0]["price"].replace('Rp', '').replace('.', '').strip())
                        inPrice = ui.input(label='Item Price', value=formatedPrice) \
                            .props('type=number dense outlined') \
                            .classes('flex-1 text-sm').bind_visibility_from(userInfo['isAdmin'])
                        ui.button('Update Price', on_click=onUpdatePrice)\
                            .classes('text-sm px-3 py-1 rounded-md')

                    outQty = ui.input(label='Quantity Out') \
                        .props('type=number dense outlined') \
                        .classes('flex-1 text-sm')
                    ui.button('Stock Out', on_click=onCheckout) \
                        .props('color=red dense') \
                        .classes('text-sm px-3 py-1 rounded-md')

            ui.separator()
            if userInfo['isAdmin']:
                ui.button('Delele Item', on_click=onDeleteItem) \
                    .classes('text-sm px-3 py-1 rounded-md') \
                    .props('color=amber-500 text-black')

        dialog.open()

    def ShowAddModal(self, type, userInfo):
        print(type)

        dialog = ui.dialog()

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):
            with ui.row().classes('w-full h-screen items-center justify-center') as container:
                ui.label('Loading Data...')
                ui.spinner('dots', size='lg', color='red')
            form_container = ui.column().classes('hidden')

            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            async def init_form():
                unit_options = {u['guid']: u['name'] for u in business.GetUnit()}
                first_guid = next(iter(unit_options))

                with form_container:
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

                            ui.label('Packaging Unit')
                            radio = ui.radio(unit_options, value=first_guid).props('inline')

                            ui.label('Product Price')
                            itemPrice = ui.input(label='Item price') \
                                .props('type=number dense outlined') \
                                .classes('flex-1 text-sm')

                            ui.label('Product Description')
                            description = ui.textarea(label='Description') \
                                .props('dense outlined') \
                                .classes('flex-1 text-sm')

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
                                ui.navigate.to('/warehouse')
                            else:
                                print(False)

                        ui.button('Add product', on_click=onAddItem) \
                            .classes('text-sm px-3 py-1 rounded-md') \
                            .props('color=amber-500 text-black')

                # Hide spinner and show form
                container.visible = False
                form_container.classes(remove='hidden')

            # Run async init after UI renders
            ui.timer(0.1, init_form, once=True)

        dialog.open()

    def ShowAddMenuModal(self, ingredients, categories, units):
        categoryRef = [None]
        ingredientRef = [None]
        unitRef = [None]
        ingredientContainer = [None]
        ingredientDatas = []
        ingredientDropdown = []

        dialog = ui.dialog().props('maximized')
        textInput = []

        def categoryLabel(new_label: str):
            categoryRef[0].props(f'label={new_label}')
            categoryRef[0].update()
            ui.notify(f'You selected {new_label}')

        def ingredientLabel(new_label: str):
            ingredientRef[0].props(f'label={new_label}')
            ingredientRef[0].update()
            ui.notify(f'Selected ingredient: {new_label}')

        def unitLabel(new_label: str):
            unitRef[0].props(f'label={new_label}')
            unitRef[0].update()
            ui.notify(f'selected unit: {new_label}')

        def getIngredient(name):
            print(name)

        def getValue(name):
            nonlocal ingredientDatas
            value = next((val['value'] for val in categories if val['name'] == name), None)

            if value is not None:
                for ingredient in ingredients:
                    if ingredient['type'] == value:
                        ingredientDatas = ingredient['data']
                        break
                else:
                    ingredientDatas = []

            print('Updated ingredientDropdown:', ingredientDatas)

            if ingredientContainer[0]:
                ingredientContainer[0].clear()

                if ingredientDatas:
                    for ingredient in ingredientDatas:
                        item_name = ingredient['name']
                        with ingredientContainer[0]:
                            ui.item(item_name, on_click=lambda name=item_name: (
                                getIngredient(name),
                                ingredientLabel(name)
                            ))
                else:
                    with ingredientContainer[0]:
                        ui.item('No data found', on_click=lambda: ui.notify('No data was found'))

            print(ingredientDropdown)



        def AddIngredient():
            with ui.grid(columns=4).classes('gap-4'):
                with ui.dropdown_button('Category', auto_close=True) as dropdown:
                    categoryRef[0] = dropdown
                    for category in categories:
                        name = category['name']
                        ui.item(name, on_click=lambda name=name: (getValue(name), categoryLabel(name)))

                with ui.dropdown_button('Ingredient', auto_close=True) as dropdown:
                    ingredientRef[0] = dropdown
                    container = ui.element('div')  # plain HTML div for dynamic items
                    ingredientContainer[0] = container

                ui.input(label=f'Ingredient{len(textInput) + 1}') \
                    .props('dense outlined') \
                    .classes('w-60 text-sm')

                with ui.dropdown_button('Unit', auto_close=True):
                    for unit in units:
                        name = unit['name']
                        ui.item(name, on_click=lambda name=name: unitLabel(name))

        with dialog, ui.card().classes('w-full h-full p-6 max-w-none shadow-xl'):
            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            with ui.stepper().props('vertical').classes('w-full') as stepper:
                with ui.step('Product Name'):
                    ui.label('Name of your product')
                    with ui.grid(columns=2).classes('gap-2'):
                        ui.label('Product Name')
                        productName = ui.input(label='Product Name') \
                            .props('dense outlined') \
                            .classes('w-60 text-sm')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)


                with ui.step('Ingredient'):
                    ui.label('Input Ingredient')
                    ui.button('Add', on_click=AddIngredient) \
                        .classes('text-sm px-3 py-1 rounded-md') \
                        .props('color=amber-500 text-black')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)
                        ui.button('Back', on_click=stepper.previous).props('flat')


                with ui.step('Bake'):
                    ui.label('Bake for 20 minutes')
                    with ui.stepper_navigation():
                        ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
                        ui.button('Back', on_click=stepper.previous).props('flat')

        dialog.open()