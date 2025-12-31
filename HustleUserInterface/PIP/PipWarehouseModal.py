from nicegui import ui
from Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Business
from Business.Pip.PipBusiness import PipBusiness as Pip

business = Business()
pip = Pip()

class PipWarehouseModal():
    def __init__(self) -> None:
        pass

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
                pip_options_list = pip.GetPip()
                pip_options = {p["guid"]: p["name"] for p in pip_options_list}
                product_data = {p["guid"]: p for p in pip_options_list}

                unit_options = {u["guid"]: u["name"] for u in business.GetUnit()}
                first_unit_guid = next(iter(unit_options)) if unit_options else None
                first_product_guid = next(iter(pip_options)) if pip_options else None

                with form_container:
                    ui.label('Add new item').classes('text-2xl font-semibold text-gray-800')
                    ui.separator()

                    with ui.column().classes('relative p-4 border rounded-md'):
                        with ui.grid(columns=2).classes('gap-3'):
                            ui.label('Product Name')
                            product_name = ui.select(pip_options, value=first_product_guid) \
                                .props('dense outlined') \
                                .classes('w-60 text-sm')

                            ui.label('Product In')
                            stockIn = ui.input(label='Stock in',
                                               value=product_data.get(first_product_guid, {}).get("stock", 0)) \
                                .props('type=number dense outlined') \
                                .classes('flex-1 text-sm')

                            ui.label('Product Packaging')
                            packaging = ui.input(label='Packaging',
                                                 value=product_data.get(first_product_guid, {}).get("packaging", 0)) \
                                .props('type=number dense outlined') \
                                .classes('flex-1 text-sm')

                            ui.label('Packaging Unit')
                            radio = ui.radio(unit_options, value=first_unit_guid).props('inline')

                            ui.label('Product Price')
                            itemPrice = ui.input(label='Item price',
                                                 value=product_data.get(first_product_guid, {}).get("price", 0)) \
                                .props('type=number dense outlined') \
                                .classes('flex-1 text-sm')

                            ui.label('Product Description')
                            description = ui.textarea(label='Description') \
                                .props('dense outlined') \
                                .classes('flex-1 text-sm')

                            def on_product_change():
                                selected_guid = product_name.value
                                data = product_data.get(selected_guid, {})
                                stockIn.value = data.get("stock", 0)
                                packaging.value = data.get("packaging", 0)
                                itemPrice.value = data.get("price", 0)
                                stockIn.update()
                                packaging.update()
                                itemPrice.update()

                            product_name.on('update:modelValue', lambda e: on_product_change())

                            def onAddItem():
                                selected_guid = product_name.value
                                data = product_data.get(selected_guid, {})
                                value = {
                                    "type": type,
                                    "data": {
                                        "name": data.get("name", ""),
                                        "stockIn": stockIn.value,
                                        "packaging": packaging.value,
                                        "price": itemPrice.value,
                                        "description": description.value,
                                        "unit": radio.value,
                                        "updatedBy": userInfo["name"]
                                    }
                                }
                                print("input value: ", value)

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


