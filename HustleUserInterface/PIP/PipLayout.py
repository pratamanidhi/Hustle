from nicegui import ui
from PIP.PipModal import PipModal as Modal
from Business.Pip.PipBusiness import PipBusiness as Business
import json

modal = Modal()
business = Business()

class PipLayout():
    def __init__(self) -> None:
        pass

    def PipContent(self, allStocks, ingredients, units, user):
        def addNewPip():
            modal.AddPip(allStocks, ingredients, units, user)

        content_container = ui.column().classes('w-full h-full')
        with content_container:
            with ui.splitter(value=10).classes('w-full h-full') as splitter:
                with splitter.before:
                    with ui.tabs().props('vertical').classes('w-50') as tabs:
                        list_tab = ui.tab('Supplier List')

                with splitter.after:
                    with ui.tab_panels(tabs, value=list_tab).props('vertical').classes('w-full h-full'):
                        with ui.tab_panel(list_tab):
                            with ui.grid(columns=2).classes('gap-5'):
                                ui.button('Add new PIP', on_click=addNewPip) \
                                    .props('flat dense')

                            ui.separator()
                            ui.label("List of PIP").classes('font-semibold text-gray-800')
                            with ui.column().classes('w-full'):
                                self.ShowPipData()

    def ShowPipData(self):
        result = business.GetPip()

        rows = []

        for pip in result:
            ingredientDatas = []
            ingredientsJson = json.loads(pip['ingredient'].replace("'", '"'))

            for ingredient in ingredientsJson:
                datas = {
                    'ingredient': ingredient['selectedIngredient'],
                    'dose': f"{ingredient['doseInput']} {ingredient['selectedUnit']}"
                }
                ingredientDatas.append(datas)

            rows.append({
                "name": pip['name'],
                "ingredient": ingredientDatas,
                "price": f"Rp. {pip['price']}"
            })

        parent_columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name'},
            {'name': 'ingredient', 'label': 'Ingredient', 'field': 'ingredient'},
            {'name': 'price', 'label': 'Price', 'field': 'price'},
            {'name': 'action', 'label': 'Action', 'align': 'center'},
        ]

        ingredient_columns = [
            {'name': 'ingredient', 'label': 'Ingredient', 'field': 'ingredient'},
            {'name': 'dose', 'label': 'Dose', 'field': 'dose'},
        ]

        ingredient_columns_json = json.dumps(ingredient_columns)

        def onDelete(args):
            print(args['name'])
            result = business.DeletePip(args['name'])
            if result == True:
                ui.notify(f" {args['name']} deleted!")
                ui.navigate.to('/pip')
            else:
                ui.notify(f" {args['name']} failed to delete!")

        table = ui.table(columns=parent_columns, rows=rows).style('width: 100%; table-layout: fixed;')
        table.add_slot(
            'body-cell-ingredient',
            f"""
                <q-td :props="props" style="padding: 0;">
                  <div style="width: 100%; min-width: 600px; overflow-x: auto; margin-top: 10px; margin-bottom: 10px;">
                    <q-table
                      dense
                      flat
                      bordered
                      :columns='{ingredient_columns_json}'
                      :rows="props.row.ingredient"
                      row-key="ingredient"
                      style="width: 100%;"
                    />
                  </div>
                </q-td>
            """
        )
        # other slots...
        table.add_slot(
            'body-cell-action',
            '''
                <q-td :props="props">
                  <q-btn flat color="red" size="sm" label="Delete" @click="$parent.$emit('delete', props.row)" />
                </q-td>
            '''
        )
        table.on('delete', lambda e: onDelete(e.args))



