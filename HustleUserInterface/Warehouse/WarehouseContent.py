from datetime import datetime
from nicegui import ui
from HustleUserInterface.API.Warehouse.WarehouseAPI import WarehouseAPI as wh
from HustleUserInterface.Common.StockEnum import StockEnum as enum
from HustleUserInterface.Common.Modal.ModalElement import ModalElement as modal


def get_columns():
    return [
        {'name': 'name', 'label': 'Name', 'field': 'name'},
        {'name': 'stockIn', 'label': 'Stock In', 'field': 'stockIn', 'icon': 'add_shopping_cart'},
        {'name': 'stockOut', 'label': 'Stock Out', 'field': 'stockOut', 'icon': 'remove_shopping_cart'},
        {'name': 'totalStock', 'label': 'Total Stock', 'field': 'totalStock', 'icon': 'inventory'},
        {'name': 'updatedBy', 'label': 'Last Updated By', 'field': 'updatedBy', 'icon': 'person'},
        {'name': 'action', 'label': 'Action', 'field': 'action', 'icon': 'edit'},
    ]


def get_stock_data(stock_type):
    rows = wh().GetStock(stock_type)
    formatted_rows = []
    for row in rows:
        new_row = row.copy()
        if new_row.get('lastInput'):
            try:
                dt_object = datetime.fromisoformat(new_row['lastInput'])
                new_row['lastInput'] = dt_object.strftime('%Y-%b-%d %H:%M:%S')
            except ValueError:
                new_row['lastInput'] = 'Invalid Date'
        else:
            new_row['lastInput'] = '-'

        if new_row.get('lastOutput'):
            try:
                dt_object = datetime.fromisoformat(new_row['lastOutput'])
                new_row['lastOutput'] = dt_object.strftime('%Y-%b-%d %H:%M:%S')
            except ValueError:
                new_row['lastOutput'] = 'Invalid Date'
        else:
            new_row['lastOutput'] = '-'

        if new_row.get('price') is not None:
            try:
                price_value = int(new_row['price'])
                formatted_price = f"Rp {price_value:,.0f}".replace(",", ".")
                new_row['price'] = formatted_price
            except (ValueError, TypeError):
                new_row['price'] = 'N/A'
        else:
            new_row['price'] = '-'

        if new_row.get('priceUnit') is not None:
            try:
                price_value = int(new_row['priceUnit'])
                formatted_price = f"Rp {price_value:,.0f}".replace(",", ".")
                new_row['priceUnit'] = formatted_price
            except (ValueError, TypeError):
                new_row['priceUnit'] = 'N/A'
        else:
            new_row['price'] = '-'

        formatted_rows.append(new_row)

    return get_columns(), formatted_rows


def render_stock_table(stock_type, title):
    with ui.column().classes('w-full max-w-screen-md'):
        ui.label(title).classes('text-lg font-bold mb-2')
        columns, rows = get_stock_data(stock_type)

        table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full')

        # Header slot
        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    <div class="flex items-center justify-start">
                        <q-icon :name="col.icon" size="sm" class="q-mr-xs" />
                        {{ col.label }}
                    </div>
                </q-th>
            </q-tr>
        ''')

        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width>
                    <q-btn size="sm" color="accent" round dense
                        @click="props.expand = !props.expand"
                        :icon="props.expand ? 'remove' : 'add'" />
                </q-td>

                <q-td v-for="col in props.cols" :key="col.name" :props="props">
                    <q-badge 
                        v-if="col.name === 'totalStock'" 
                        :color="(props.row[col.field] ?? 0) < 2 ? 'red' : 'green'">
                        {{ props.row[col.field] ?? '-' }}
                    </q-badge>

                    <q-btn 
                        v-else-if="col.name === 'action'" 
                        color="primary" size="sm" 
                        label="Edit" 
                        @click="() => $parent.$emit('edit', props.row)" />

                    <span v-else>{{ props.row[col.field] ?? '-' }}</span>
                </q-td>
            </q-tr>

            <q-tr v-show="props.expand" :props="props">
                <q-td colspan="100%">
                    div class="text-left">Last Input : {{ props.row.lastInput ?? '-' }}</div>
                    <div class="text-left">Last Output : {{ props.row.lastOutput ?? '-' }}</div>
                    <div class="text-left">Brand : {{ props.row.description ?? '-' }}</div>
                    <div class="text-left">Packaging : {{ props.row.packaging ?? '-' }} {{ props.row.unit ?? '' }}</div>
                    <div class="text-left">Item price : {{ props.row.price ?? '-' }}</div>
                    <div class="text-left">Price per unit : {{ props.row.priceUnit ?? '-' }}</div>

                </q-td>
            </q-tr>
        ''')

        def handle_edit(event):
            row = event.args
            modal().ShowModal(row,stock_type)

        table.on('edit', handle_edit)


def showCheckOutModal(datas):
    dialog = ui.dialog()

    with dialog, ui.column().classes('p-4 space-y-2 bg-white rounded-lg shadow-lg'):
        ui.label('Check out').classes('text-lg font-bold')
        ui.label(f"Name: {datas.get('name', '-')}")
        ui.label(f"Total Stock: {datas.get('totalStock', '-')}")
        ui.label(f"Brand: {datas.get('description', '-')}")
        ui.button('Close', on_click=dialog.close)

    dialog.open()




@ui.page('/')
def WarehouseContent():
    with ui.row().classes('w-full justify-evenly'):
        render_stock_table(enum.Coffee, 'Coffee Stock')
        render_stock_table(enum.Juice, 'Juice Stock')
        render_stock_table(enum.MilkAndCream, 'Milk And Cream Stock')
        render_stock_table(enum.Powder, 'Powder Stock')
        render_stock_table(enum.Syrup, 'Syrup Stock')
        render_stock_table(enum.Tea, 'Tea Stock')
        render_stock_table(enum.Topping, 'Topping Stock')
        render_stock_table(enum.Other, 'Other Stock')