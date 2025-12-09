from nicegui import ui
from Business.Pip.PipBusiness import PipBusiness as Business

business = Business()


class PipModal():
    def __init__(self) -> None:
        pass

    def AddPip(self, ingredients, categories, units):
        dialog = ui.dialog().props('maximized')

        def categoryForm():
            return {category["value"]: category["name"] for category in categories}

        def unitForm():
            return {unit["guid"]: unit["name"] for unit in units}

        def ingredientForm(category_id):
            option = {}
            for ingredient in ingredients:
                if ingredient["type"] == category_id:
                    for ingredientData in ingredient["data"]:
                        option[f"{ingredientData['guid']} ({ingredientData['priceUnit']})"] = ingredientData['name']
            return option

        categoryDatas = categoryForm()
        unitDatas = unitForm()

        inputFormContainer = None
        ingredientListContainer = None
        listOfIngredients = None
        productionCost = None


        ingredientForms = []
        listOfIngredient = []


        def inputForm():
            formData = {
                'category': '',
                'ingredient': '',
                'price': 0,
                'doseInput': None,
                'selectedUnit': None,
                'selectedIngredient': None,
            }
            ingredientForms.append(formData)

            with inputFormContainer:
                with ui.grid(columns=4).classes('gap-3'):

                    def onChangeCategory(e, formData=formData):
                        formData['category'] = e.value
                        options = ingredientForm(e.value)
                        ingredient_placeholder.clear()
                        with ingredient_placeholder:
                            formData['selectedIngredient'] = ui.select(
                                options=options,
                                with_input=True,
                                on_change=lambda ev: onChangeIngredient(ev, formData),
                                label='Ingredient'
                            ).props('dense outlined').classes('w-60 text-sm')

                    def onChangeIngredient(e, formData=formData):
                        formData['ingredient'] = e.value
                        selected_guid = e.value.split(' ')[0]
                        for ingredient in ingredients:
                            for ingredientData in ingredient['data']:
                                if ingredientData['guid'] == selected_guid:
                                    price = int(ingredientData['priceUnit'].replace('Rp', '').replace('.', '').strip())
                                    formData['price'] = price
                                    return

                    ui.select(
                        options=categoryDatas,
                        with_input=True,
                        on_change=onChangeCategory,
                        label='Category'
                    ).props('dense outlined').classes('w-60 text-sm')

                    ingredient_placeholder = ui.row()

                    with ingredient_placeholder:
                        formData['selectedIngredient'] = ui.select(
                            options={}, with_input=True,
                            on_change=lambda e: onChangeIngredient(e, formData),
                            label='Ingredient'
                        ).props('dense outlined').classes('w-60 text-sm')

                    formData['doseInput'] = ui.input(label='Dose').props('type=number dense outlined').classes(
                        'w-60 text-sm')
                    formData['selectedUnit'] = ui.select(
                        options=unitDatas,
                        with_input=True,
                        label='Unit'
                    ).props('dense outlined').classes('w-60 text-sm')

        def onAddItem():
            inputForm()

        def onSubmitAll():
            nonlocal productionCost
            nonlocal listOfIngredients
            listOfIngredient.clear()

            for form in ingredientForms:
                dose = form['doseInput'].value if hasattr(form['doseInput'], 'value') else form['doseInput']
                unit = form['selectedUnit'].value if hasattr(form['selectedUnit'], 'value') else form['selectedUnit']
                ing = form['selectedIngredient'].value if hasattr(form['selectedIngredient'], 'value') else form[
                    'selectedIngredient']

                listOfIngredient.append({
                    'doseInput': dose,
                    'selectedUnit': unit,
                    'selectedIngredient': ing,
                    'price': form['price']  # keep the original data
                })

            ingredientListContainer.clear()
            with ingredientListContainer:
                listOfIngredients = self.DevelopPip(listOfIngredient, ingredients, units)
                ui.separator()
                totalProductionCost = sum(item['price'] * int(item['doseInput']) for item in listOfIngredient)
                productionCost = self.ProductionCost(totalProductionCost)

        def onSave():
            ingredient = str(listOfIngredients)
            datas = {
                "name" : productName.value,
                "ingredient": ingredient,
                "price": productionCost['value']
            }
            result = business.InputPip(datas)
            if result:
                ui.notify("Success to save PIP data")
                dialog.close()
                ui.navigate.to('/pip')
            else:
                ui.notify("Failed to save PIP")


        with dialog, ui.card().classes('w-full h-full p-6 max-w-none shadow-xl'):
            ui.button(icon='close', on_click=dialog.close).props('flat round dense color=grey').classes(
                'absolute top-2 right-2 z-10')

            ui.separator()

            with ui.grid(columns=2).classes('gap-3'):
                ui.label('Product Name')
                productName = ui.input(label='Name') \
                    .props('dense outlined') \
                    .classes('w-60 text-sm')

            ui.separator()

            inputFormContainer = ui.column().classes('gap-4')
            inputForm()
            with ui.row().classes('gap-2 mt-4'):
                ui.button('Add item', on_click=onAddItem).classes('text-sm px-3 py-1 rounded-md').props(
                    'color=amber-500 text-black')
                ui.button('Submit All', on_click=onSubmitAll).classes('text-sm px-3 py-1 rounded-md').props(
                    'color=green text-white')


            ingredientListContainer = ui.column().classes('gap-2 mt-2')
            ingredientListContainer

            with ui.row().classes('gap-2 mt-4'):
                ui.button('Save', on_click=onSave).props('color=green text-white')

        dialog.open()

    def DevelopPip(self, listOfIngredient, ingredients, units):
        row = []

        for i, ingredient in enumerate(listOfIngredient, 1):
            ingredient['selectedIngredient'] = ingredient['selectedIngredient'].split(' ')[0]

            for ingredientList in ingredients:
                for ingredientData in ingredientList['data']:
                    if ingredientData['guid'] == ingredient['selectedIngredient']:
                        ingredient['selectedIngredient'] = ingredientData['name']

            for unit in units:
                if unit.get('guid') == ingredient['selectedUnit']:
                    ingredient['selectedUnit'] = unit.get('name')

            datas = {
                'id': i,
                'ingredient': ingredient['selectedIngredient'],
                'dose': ingredient['doseInput'],
                'unit': ingredient['selectedUnit'],
                'price': f'Rp. {ingredient["price"]}',
                'totalCost': f'Rp. {int(ingredient["price"]) * int(ingredient["doseInput"])}'
            }
            row.append(datas)

        ui.label('Summary of the ingredient')
        columns = [
            {'name': 'id', 'label': 'No', 'field': 'id', 'required': True, 'align': 'left'},
            {'name': 'ingredient', 'label': 'Ingredient', 'field': 'ingredient', 'required': True,
             'align': 'left'},
            {'name': 'dose', 'label': 'Dose', 'field': 'dose', 'sortable': False},
            {'name': 'unit', 'label': 'Unit', 'field': 'unit', 'sortable': False},
            {'name': 'price', 'label': 'Price PerMl', 'field': 'price', 'sortable': False},
            {'name': 'totalCost', 'label': 'Total Cost', 'field': 'totalCost', 'sortable': False},
        ]
        ui.table(columns=columns, rows=row, row_key='name')
        return listOfIngredient

    def ProductionCost(self, TotalProductionCost):

        result = {'value': None}

        ui.separator()

        def calculate():
            total = int(sellingInput.value) + int(TotalProductionCost)
            finalPrice.text = f'Rp {total}'
            result['value'] = total
            return total

        with ui.grid(columns=2).classes('gap-3'):
            ui.label('Production Cost')
            ui.label(f'Rp {TotalProductionCost}')

            ui.label('Fix Price')
            sellingInput = ui.input(label='Selling Price') \
                .props('type=number dense outlined') \
                .classes('w-60 text-sm')

            ui.button('Calculate Pip', on_click=calculate) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

        ui.separator()

        with ui.grid(columns=2).classes('gap-3'):
            ui.label('Final pricing point')
            finalPrice = ui.label('Rp 0').classes('text-green-600 font-bold text-2xl')

        return result