import json

from nicegui import ui
from HustleUserInterface.API.Common.CommonAPI import CommonApi as Common
from HustleUserInterface.API.Business.BusinessAPI import BusinessAPI as Business
from HustleUserInterface.API.Warehouse.WarehouseAPI import WarehouseAPI as Warehouse


class ModalElement:
    def __init__(self) -> None:
        pass

    def ShowModal(self, datas, type):
        print(datas)
        if isinstance(datas, dict):
            datas = [datas]

        dialog = ui.dialog()

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name'},
            {'name': 'description', 'label': 'Description', 'field': 'description'},
            {'name': 'stockOut', 'label': 'Stock Out', 'field': 'stockOut'},
            {'name': 'totalStock', 'label': 'Total Stock', 'field': 'totalStock'}
        ]

        rows = [
            {
                'name': str(d.get('name', '')),
                'description': str(d.get('description', '')),
                'stockOut': str(d.get('stockOut', '')),
                'totalStock': str(d.get('totalStock', '')),
            }
            for d in datas
        ]

        def onCheckout():
            quantity = inputQty.value
            isOut = True
            print(f'Quantity: {quantity}')
            print(f'Datas: {datas}')
            print(f'Type: {type}')
            for i in datas:
                price = i['price']
                priceUnit = i['priceUnit']
                lastInput = i['lastInput']
                lastOutput = i['lastOutput']

                formatedPrice = int(price.replace('Rp','').replace('.','').strip())
                formatedPriceUnit = int(priceUnit.replace('Rp', '').replace('.','').strip())

                i['price'] = formatedPrice
                i['priceUnit'] = formatedPriceUnit
                i['lastInput'] = None
                i['lastOutput'] = None
                i['stockOut'] = int(quantity)

                print(json.dumps(i))
                result = Warehouse().CheckOutStock(type, isOut, i)
                if result is True:
                    print(True)
                    dialog.close()
                else:
                    print(False)


        with dialog, ui.card().classes('w-full max-w-screen-md p-4 space-y-4'):
            ui.label('Check out').classes('text-lg font-bold')

            ui.table(columns=columns, rows=rows, row_key='name').classes('w-full')

            with ui.row().classes('w-full border items-center'):
                ui.button('Close', on_click=dialog.close).props('color=secondary')
                ui.space()
                inputQty = ui.input(label='Quantity').props('type=number')
                ui.button('Check Out', on_click=onCheckout).props('color=red')

        dialog.open()

    def ModalInputMenu(self):
        categories = []
        ingredients = {}

        categoryDatas = Common().Category()
        if categoryDatas is not None:
            categories = {i['value']: i['name'] for i in categoryDatas}

        dialog = ui.dialog()
        ui.button('Open Table Dialog', on_click=dialog.open)
        row_container = None

        def add_row():
            nonlocal ingredients

            ingredient_select = None
            def onCategoryChange(e):
                nonlocal ingredients
                ingredient = Business().GetIngredient(e.value)

                if ingredient is not None:
                    ingredients = {i['priceUnit']: i['name'] for i in ingredient}
                    if ingredient_select:
                        ingredient_select.options = ingredients
                        ingredient_select.update()
                print(f'Selected category value: {e.value}')

            def onIngredientChange(e):
                print(f'Selected ingredient value: {e.value}')

            with row_container:
                with ui.row().classes('items-center gap-4'):
                    ui.select(categories, label='Category', value=None, on_change=onCategoryChange)
                    ingredient_select = ui.select(ingredients, label='Ingredient', value=None,
                                                  on_change=onIngredientChange)
                    ui.input(label='Number').props('type=number')

        with dialog:
            with ui.card().classes('w-full max-w-screen-md p-4 space-y-4'):
                ui.label('Dynamic Table with Dropdowns and Number Input').classes('text-lg font-bold')
                row_container = ui.column()
                add_row()

                ui.button('Add Row', on_click=add_row).classes('mt-2')

                with ui.row().classes('justify-end mt-4'):
                    ui.button('Close', on_click=dialog.close).props('color=secondary')




