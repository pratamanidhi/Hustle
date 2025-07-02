from nicegui import ui, context
from Common.Session.Session import Session as Session
from Common.Layout.Layout import Layout as Layout


session = Session()
layout = Layout()
@ui.page('/home')
def HomeContent():
    with ui.row().classes('w-full h-screen items-center justify-center') as container:
        ui.label('Loading Data..')
        ui.spinner('dots', size='lg', color='red')

    async def Init():
        result = await session.Session()
        if result is not False:
            layout.Header(result)

            ui.label(f'Hi! {result['name']}, Welcome to Hustle management system')
            container.visible = False
        else:
            ui.notify("No login info found", type='warning')
            ui.navigate.to('/')

    ui.timer(0.1, Init, once=True)



