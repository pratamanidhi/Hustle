from nicegui import ui
from Common.Button import Button as Button
from HustleUserInterface.Common.Modal.ModalElement import ModalElement as Modal
from Business.Report.ReportBusiness import ReportBusiness as Report
from Common.StockEnum import StockEnum
from datetime import datetime


modal = Modal()
button = Button()
report = Report()
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

                def goToReport():
                    ui.navigate.to('/report')

                ui.button('Home', on_click=goToHome).props('flat dense')
                ui.button('Warehouse', on_click=goToWarehouse).props('flat dense')
                if datas['isAdmin']:
                    ui.button('Menu', on_click=goToMenu).props('flat dense')
                    ui.button('Report', on_click=goToReport).props('flat dense')



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
                    modal.ShowAddModal(stockType, userInfo)

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

    def GetReportMainContent(self):
        content_container = ui.column().classes('w-full h-full')

        def renderContent():
            with ui.row().classes('w-full min-h-16 items-center justify-center gap-2') as container:
                ui.label('Loading Data..')
                ui.spinner('dots', size='lg', color='red')

            content_container.clear()

            data = report.GetAllReport()

            with content_container:
                with ui.splitter(value=10).classes('w-full h-full') as splitter:
                    with splitter.before:
                        with ui.tabs().props('vertical').classes('w-50') as tabs:
                            chart = ui.tab('Chart Report', icon='bar_chart')
                            table = ui.tab('Table Report', icon='view_list')

                    with splitter.after:
                        with ui.input('Date') as date:
                            with ui.menu().props('no-parent-event') as menu:
                                with ui.date().bind_value(date):
                                    with ui.row().classes('justify-end'):
                                        ui.button('Close', on_click=menu.close).props('flat')
                            with date.add_slot('append'):
                                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

                        ui.button('Add new', on_click=UpdateDatas).props('flat dense')

                        with ui.tab_panels(tabs, value=chart) \
                                .props('vertical').classes('w-full h-full'):
                            with ui.tab_panel(chart):
                                for reportValue in data:
                                    self.RenderChartReport(reportValue)
                            with ui.tab_panel(table):
                                for reportValue in data:
                                    self.RenderTableReport(reportValue)
            container.visible = False

        def UpdateDatas():
            ui.notify('Update clicked')
            renderContent()

        renderContent()


    def RenderChartReport(self, datas):
        ui.separator()
        ui.label(datas['name'])

        chart = ui.highchart({
            'title': datas['name'],
            'chart': {'type': 'bar'},
            'xAxis': {'categories': ['Stock In', 'Stock Out']},
            'series': [],
        }).classes('w-full h-64')

        def loadData():
            reports = datas['data']
            charts = []
            if reports is not None:
                for reportData in reports:
                    data = []
                    if reportData['stockIn'] is not None:
                        data.append(reportData['stockIn'])
                    if reportData['stockOut'] is not None:
                        data.append(reportData['stockOut'])

                    charts.append({
                        'name': reportData['name'],
                        'data': data,
                    })

            chart.options['series'] = charts
            chart.update()
            ui.separator()
        ui.timer(0.5, loadData, once=True)

    def RenderTableReport(self, datas):
        ui.separator()
        ui.label(datas['name'])

        columns = [
            {'name': 'Name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
            {'name': 'Stock In', 'label': 'Stock In', 'field': 'stockIn', 'sortable': True},
            {'name': 'Stock Out', 'label': 'Stock Out', 'field': 'stockOut', 'sortable': True},
            {'name': 'Total Transaction', 'label': 'Total Transaction', 'field': 'totalTransaction', 'sortable': True},
            {'name': 'Date', 'label': 'Date', 'field': 'date', 'sortable': True},
            {'name': 'Last Update', 'label': 'Last Update', 'field': 'lastUpdate', 'sortable': True},
        ]

        rowsData = []

        for reportData in datas['data']:
            dt_object = datetime.fromisoformat(reportData['lastUpdated'])
            data = {
                'name' : reportData['name'],
                'stockIn' : reportData['stockIn'],
                'stockOut' : reportData['stockOut'],
                'totalTransaction' : reportData['totalStockTransaction'],
                'date' : reportData['datetime'],
                'lastUpdate' : dt_object.strftime('%Y-%b-%d %H:%M:%S')
            }
            rowsData.append(data)

        ui.table(
            columns=columns,
            rows=rowsData,
            pagination={
                'rowsPerPage': 4,
                'page': 1,
            }
        ).props('multi-sort')

        ui.separator()

