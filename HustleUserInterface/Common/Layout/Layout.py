from nicegui import ui
from Common.Button import Button as Button
from HustleUserInterface.Common.Modal.ModalElement import ModalElement as Modal


modal = Modal()
button = Button()
class Layout():
    def __init__(self) -> None:
        pass

    def Header(self, datas):
        async def handleLogout():
            await button.ButtonLogout()



        with ui.header().classes('bg-[#292928] text-white'):
            with ui.element('div').classes('flex justify-between w-full items-center'):
                ui.label('Hustle Management System').classes('text-xl')
                def goToWarehouse():
                    ui.navigate.to('/warehouse')

                def goToHome():
                    ui.navigate.to('/home')

                def goToMenu():
                    ui.navigate.to('/menu')

                ui.button('Home', on_click=goToHome).props('flat dense')
                ui.button('Warehouse', on_click=goToWarehouse).props('flat dense')
                if datas['isAdmin']:
                    ui.button('Menu', on_click=goToMenu).props('flat dense')



                dropdown = ui.dropdown_button(f'Hi! {datas['name']}', auto_close=True)
                dropdown.props('color=amber-500 text-black')
                with dropdown:
                    ui.item('Logout', on_click=handleLogout)

    def DefineColumn(self):
        return [
            {'name': 'name', 'label': 'Name', 'field': 'name'},
            {'name': 'stockIn', 'label': 'Stock In', 'field': 'stockIn'},
            {'name': 'stockOut', 'label': 'Stock Out', 'field': 'stockOut'},
            {'name': 'totalStock', 'label': 'Total Stock', 'field': 'totalStock'},
            {'name': 'updatedBy', 'label': 'Last Updated By', 'field': 'updatedBy'},
            {'name': 'action', 'label': 'Action', 'field': 'action'},
        ]

    def RenderTable(self, stockType, title, userInfo, datas):
        with ui.column().classes('w-full max-w-screen-md'):
            ui.label(title).classes('text-lg font-bold mb-2')

            if userInfo['isAdmin']:
                def CreateNewItem():
                    modal().ShowAddModal(stockType, userInfo)

                ui.button('Add new', on_click=CreateNewItem) \
                    .props('flat dense')
                ui.separator()

            columns = self.DefineColumn()
            rows = datas
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
                modal.ShowModal(row, stockType, userInfo)

            table.on('edit', handle_edit)
            ui.separator()

