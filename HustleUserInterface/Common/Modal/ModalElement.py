from nicegui import ui
from HustleUserInterface.Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Business
from Business.Common.CommonBusiness import CommonBusiness as CommonBusiness
from starlette.formparsers import MultiPartParser
from datetime import datetime, date
from HustleUserInterface.Business.DialIn.DialInBussiness import DialInBussiness as DialIn

business = Business()
commonBusiness = CommonBusiness()
dialIn = DialIn()


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

        if userInfo["isAdmin"]:
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
            if userInfo["isAdmin"]:
                row["stockIn"] = str(d.get('stockIn'))
            rows.append(row)

        def onCheckout():
            datas[0]["updatedBy"] = userInfo["name"]
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

        if userInfo["isAdmin"]:
            def onCheckin():
                datas[0]["updatedBy"] = userInfo["name"]
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

            if userInfo["isAdmin"]:
                ui.label('Manage Stock').classes('text-2xl font-semibold text-gray-800')
            else:
                ui.label('Checkout Stock Item').classes('text-2xl font-semibold text-gray-800')

            ui.table(columns=columns, rows=rows, row_key='name').classes('w-full rounded border border-gray-300')
            ui.separator()
            with ui.column().classes('relative p-4 border rounded-md'):

                with ui.grid(columns=2).classes('gap-3'):
                    if userInfo["isAdmin"]:
                        inQty = ui.input(label='Quantity Out') \
                            .props('type=number dense outlined') \
                            .classes('flex-1 text-sm').bind_visibility_from(userInfo["isAdmin"])
                        ui.button('Stock In', on_click=onCheckin) \
                            .classes('text-sm px-3 py-1 rounded-md')

                        formatedPrice = int(datas[0]["price"].replace('Rp', '').replace('.', '').strip())
                        inPrice = ui.input(label='Item Price', value=formatedPrice) \
                            .props('type=number dense outlined') \
                            .classes('flex-1 text-sm').bind_visibility_from(userInfo["isAdmin"])
                        ui.button('Update Price', on_click=onUpdatePrice) \
                            .classes('text-sm px-3 py-1 rounded-md')

                    outQty = ui.input(label='Quantity Out') \
                        .props('type=number dense outlined') \
                        .classes('flex-1 text-sm')
                    ui.button('Stock Out', on_click=onCheckout) \
                        .props('color=red dense') \
                        .classes('text-sm px-3 py-1 rounded-md')

            ui.separator()
            if userInfo["isAdmin"]:
                ui.button('Delete Item', on_click=onDeleteItem) \
                    .classes('text-sm px-3 py-1 rounded-md') \
                    .props('color=amber-500 text-black')

        dialog.open()

    def ShowAddModal(self, type, userInfo):
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
                unit_options = {u["guid"]: u["name"] for u in business.GetUnit()}
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
                                    "updatedBy": userInfo["name"]
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

                container.visible = False
                form_container.classes(remove='hidden')

            ui.timer(0.1, init_form, once=True)

        dialog.open()

    def ShowAddMenuModal(self, ingredients, categories, units):
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
            listOfIngredient.clear()
            for form in ingredientForms:
                form['doseInput'] = form['doseInput'].value if form['doseInput'] else ''
                form['selectedUnit'] = form['selectedUnit'].value if form['selectedUnit'] else ''
                form['selectedIngredient'] = form['selectedIngredient'].value if form['selectedIngredient'] else ''
                listOfIngredient.append(form)

            ingredientListContainer.clear()
            with ingredientListContainer:
                self.DevelopMenu(listOfIngredient, ingredients, units)

                ui.separator()

                totalProductionCost = sum(item['price'] * int(item['doseInput']) for item in listOfIngredient)
                self.ProductionCost(totalProductionCost)

        with dialog, ui.card().classes('w-full h-full p-6 max-w-none shadow-xl'):
            ui.button(icon='close', on_click=dialog.close).props('flat round dense color=grey').classes(
                'absolute top-2 right-2 z-10')

            with ui.stepper().props('vertical').classes('w-full') as stepper:
                with ui.step('Product Name'):
                    ui.label('Name of your product')
                    with ui.grid(columns=2).classes('gap-2'):
                        ui.label('Product Name')
                        ui.input(label='Product Name').props('dense outlined').classes('w-60 text-sm')

                        ui.label('Upload image')
                        MultiPartParser.spool_max_size = 1024 * 1024 * 5  # 5 MB
                        ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')

                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)

                with ui.step('Ingredient'):
                    ui.label('Input Ingredient')

                    inputFormContainer = ui.column().classes('gap-4')
                    inputForm()

                    with ui.row().classes('gap-2 mt-4'):
                        ui.button('Add item', on_click=onAddItem).classes('text-sm px-3 py-1 rounded-md').props(
                            'color=amber-500 text-black')
                        ui.button('Submit All', on_click=onSubmitAll).classes('text-sm px-3 py-1 rounded-md').props(
                            'color=green text-white')

                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)
                        ui.button('Back', on_click=stepper.previous).props('flat')

                with ui.step('Bake'):
                    ingredientListContainer = ui.column().classes('gap-2 mt-2')
                    ingredientListContainer

                    with ui.stepper_navigation():
                        ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
                        ui.button('Back', on_click=stepper.previous).props('flat')

        dialog.open()

    def DevelopMenu(self, listOfIngredient, ingredients, units):
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
                'price': f'Rp. {ingredient['price']}',
                'totalCost': f'Rp. {int(ingredient['price']) * int(ingredient['doseInput'])}'
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

        def calculate():
            total = int(profitInput.value) + int(TotalProductionCost)
            finalPrice.text = f'Rp {total}'

        with ui.grid(columns=2).classes('gap-3'):
            ui.label('Production Cost')
            ui.label(f'Rp {TotalProductionCost}')

            ui.label('Target Profit')
            profitInput = ui.input(label='Profit').props('type=number dense outlined').classes('w-60 text-sm')
            ui.button('Add item', on_click=calculate).classes('text-sm px-3 py-1 rounded-md').props(
                'color=amber-500 text-black')

        ui.separator()

        with ui.grid(columns=2).classes('gap-3'):
            ui.label('Final pricing point')
            finalPrice = ui.label('Rp 0').classes('text-green-600 font-bold text-2xl')

    def AddDialInModal(self, warehouseData, userData, toolsData):
        dialog = ui.dialog()
        userList = []
        toolsList = []
        coffeeList = []

        print("warehouse data: ", warehouseData)
        print("user data: ", userData)
        print("tools data: ", toolsData)

        def getUser():
            for user in userData:
                name = user['username']
                userList.append(name)

        def getTools():
            for tool in toolsData:
                name = tool['name']
                toolsList.append(name)

        def getCoffee():
            for warehouse in warehouseData:
                name = warehouse['name']
                coffeeList.append(name)

        def onAddItem():
            inputData = {
                'beansName': beansName.value,
                'roastDate': dates.value,
                'dialedBy': dialedBy.value,
                'dose': float(dose.value),
                'time': float(timing.value),
                'calibrationYield': float(calibrationYield.value),
                'sweetSpot': float(sweetSpot.value),
                'tools': tools.value,
                'grindSize': float(grindSize.value),
                'mouthFeel': mouthFeels.value,
                'black': black.value,
                'espressoNotes': espressoNotes.value,
                'americanoNotes': americanoNotes.value,
                'white': white.value,
                'cappuccinoNotes': cappuccinoNotes.value,
                'latteNotes': latteNotes.value
            }

            response = dialIn.InputDialIn(inputData)

            if response:
                dialog.close()
                ui.notify("Success to save dial-in data")
                ui.navigate.to('/home')
            else:
                ui.notify("Failed to save dial-in")

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):

            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            ui.label('Dial In Form').classes('text-2xl font-semibold text-gray-800')
            dateNow = datetime.now().strftime("%d %b %Y %H:%M")
            ui.chip( color='amber-500', removable=False).style(
                'color: white; padding-left: 8px; gap: 0.5rem').set_text(dateNow)
            ui.separator()


            with ui.tabs().classes('w-full') as tabs:
                one = ui.tab('Dial In')
                two = ui.tab('Body')
            with ui.tab_panels(tabs, value=one).classes('w-full h-[550px]'):
                with ui.tab_panel(one).classes('h-full'):
                    ui.label('Calibration').classes('text-2xl font-semibold text-gray-800')
                    ui.separator()

                    with ui.row().classes('w-full h-screen items-center justify-center'):
                        with ui.grid(columns=2).classes('gap-3'):
                            getCoffee()
                            ui.label('Beans Name')
                            beansName = ui.select(options=coffeeList, with_input=True,
                                                  on_change=lambda e: ui.notify(e.value)) \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Date')
                            ui.label(date.today().isoformat())

                            ui.label('Roast Date')
                            with ui.input('Date') as dates:
                                with ui.menu().props('no-parent-event') as menu:
                                    with ui.date().bind_value(dates):
                                        with ui.row().classes('justify-end'):
                                            ui.button('Close', on_click=menu.close).props('dense outlined')
                                with dates.add_slot('append'):
                                    ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

                            getUser()
                            ui.label('Dialed By')
                            dialedBy = ui.select(userList, multiple=True, value=[], label='Dialed By') \
                                .props('dense outlined use-chips') \
                                .classes('w-60 text-sm')

                            ui.label('Dose')
                            dose = ui.input(label='Dose') \
                                .props('type=number step=any dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Timing')
                            timing = ui.input(label='Timing') \
                                .props('type=number step=any dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Calibration Yield')
                            calibrationYield = ui.input(label='Yield') \
                                .props('type=number step=any dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Sweet Spot')
                            sweetSpot = ui.input(label='Sweet Spot') \
                                .props('type=number step=any dense outlined') \
                                .classes('w-60 text-sm')

                            getTools()
                            ui.label('Tools')
                            tools = ui.select(toolsList, multiple=True, value=[], label='Tools') \
                                .props('dense outlined use-chips') \
                                .classes('w-60 text-sm')

                            ui.label('Grind Size')
                            grindSize = ui.input(label='Grind Size') \
                                .props('type=number step=any dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Mouth Feels')
                            mouthFeels = ui.input(label='Mouth Feels') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                with ui.tab_panel(two).classes('h-full'):
                    ui.label('Notes Body').classes('text-2xl font-semibold text-gray-800')
                    ui.separator()

                    with ui.row().classes('w-full h-screen items-center justify-center'):
                        with ui.grid(columns=2).classes('gap-3'):
                            ui.label('Black')
                            black = ui.input(label='Black') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Espresso')
                            espressoNotes = ui.textarea(label='Espresso Notes') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Americano')
                            americanoNotes = ui.textarea(label='Americano Notes') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('White')
                            white = ui.input(label='White') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Cappuccino Notes')
                            cappuccinoNotes = ui.textarea(label='Cappuccino Notes') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Latte Notes')
                            latteNotes = ui.textarea(label='Latte Notes') \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

            ui.button('Add product', on_click=onAddItem) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

        dialog.open()
