from datetime import datetime
from nicegui import ui, context
from HustleUserInterface.Business.Warehouse.WarehouseBusiness import WarehouseBusiness as Warehouse
from HustleUserInterface.Common.Button import Button as Button
from HustleUserInterface.Common.StockEnum import StockEnum as enum
from HustleUserInterface.Common.Modal.ModalElement import ModalElement as modal
from Common.Layout.Layout import Layout as Layout
from Common.Session.Session import Session as Session
import json


warehouse = Warehouse()
button = Button()
layout = Layout()
session = Session()
def GetColumn():
    return [
        {'name': 'name', 'label': 'Name', 'field': 'name'},
        {'name': 'stockIn', 'label': 'Stock In', 'field': 'stockIn'},
        {'name': 'stockOut', 'label': 'Stock Out', 'field': 'stockOut'},
        {'name': 'totalStock', 'label': 'Total Stock', 'field': 'totalStock'},
        {'name': 'updatedBy', 'label': 'Last Updated By', 'field': 'updatedBy'},
        {'name': 'action', 'label': 'Action', 'field': 'action'},
    ]

def TableRender(stock_type, title, userInfo):
    with ui.column().classes('w-full max-w-screen-md'):
        ui.label(title).classes('text-lg font-bold mb-2')

        if userInfo['isAdmin']:
            def CreateNewItem():
                modal().ShowAddModal(stock_type, userInfo)

            ui.button('Add new', on_click=CreateNewItem)\
                    .props('flat dense')
            ui.separator()

        columns = GetColumn()
        rows = warehouse.GetStock(stock_type)
        table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full')
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
                        color="amber-500" size="sm" 
                        label="Edit" 
                        @click="() => $parent.$emit('edit', props.row)" />

                    <span v-else>{{ props.row[col.field] ?? '-' }}</span>
                </q-td>
            </q-tr>

            <q-tr v-show="props.expand" :props="props">
                <q-td colspan="100%">
                    <div class="text-left">Last Input : {{ props.row.lastInput ?? '-' }}</div>
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
            modal().ShowModal(row,stock_type, userInfo)

        table.on('edit', handle_edit)
        ui.separator()


@ui.page('/warehouse')
def WarehouseContent():
    with ui.row().classes('w-full h-screen items-center justify-center') as container:
        ui.label('Loading Data..')
        ui.spinner('dots', size='lg', color='red')

    async def init():
        result = await session.Session()
        if result is not False:
            layout.Header(result)

            with ui.row().classes('w-full justify-evenly'):
                TableRender(enum.Coffee, 'Coffee Stock', result)
                TableRender(enum.Juice, 'Juice Stock', result)
                TableRender(enum.MilkAndCream, 'Milk And Cream Stock', result)
                TableRender(enum.Powder, 'Powder Stock', result)
                TableRender(enum.Syrup, 'Syrup Stock', result)
                TableRender(enum.Tea, 'Tea Stock', result)
                TableRender(enum.Topping, 'Topping Stock', result)
                TableRender(enum.Other, 'Other Stock', result)

            container.visible = False
        else:
            ui.notify("No login info found", type='warning')
            ui.navigate.to('/')

    ui.timer(0.1, init, once=True)




