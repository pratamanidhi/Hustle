from HustleUserInterface.Test.TestContent import TestContent as Content
from Common.Layout.Layout import Layout as Layout
from nicegui import ui

content = Content()
layout = Layout()
# @ui.page('/')
def Test():
    layout.Header()

    # # Main layout with sidebar and content
    # with ui.row().classes('h-screen'):
    #     # Sidebar
    #     with ui.column().classes('w-64 bg-gray-100 p-4'):
    #         ui.label('Sidebar').classes('text-lg font-bold')
    #         ui.button('Dashboard', on_click=lambda: ui.notify('Dashboard clicked'))
    #         ui.button('Logout', on_click=lambda: ui.navigate.to('/logout'))
    #
    #     # Main content
    #     with ui.column().classes('flex-1 p-4 overflow-auto'):
    #         content.TestHeader()