from nicegui import ui
from Common.Layout.Layout import Layout as Layout
from Common.Session.Session import Session as Session
from Common.StockEnum import StockEnum

layout = Layout()
session = Session()


def Content():
    @ui.page('/report')
    def ReportContent():
        with ui.row().classes('w-full h-screen items-center justify-center') as container:
            ui.label('Loading Data..')
            ui.spinner('dots', size='lg', color='red')

        async def init():
            result = await session.Session()
            if result is not False:
                layout.Header(result)
                layout.GetReportMainContent()
                container.visible = False
            else:
                ui.notify("No login info found", type='warning')
                ui.navigate.to('/')

        ui.timer(0.1, init, once=True)
