from nicegui import ui
from Business.Menu.MenuBusiness import MenuBusiness as Business
import json


business = Business()
class MenuLayout:
    def __init__(self) -> None:
        pass

    def ShowMenu(self):
        result = business.GetMenu()
        print(result)

        rows = []

        for menu in result:
            ingredientDatas = []
            ingredientsJson = json.loads(menu['ingredient'].replace("'", '"'))

            for ingredient in ingredientsJson:
                datas = {
                    'ingredient': ingredient['selectedIngredient'],
                    'dose': f"{ingredient['doseInput']} {ingredient['selectedUnit']}"
                }
                ingredientDatas.append(datas)

            rows.append({
                "name": menu['name'],
                "ingredient": ingredientDatas,
                "price": f"Rp. {menu['price']}"
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
        # table.on('delete', lambda e: onDelete(e.args))