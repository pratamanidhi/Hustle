from nicegui import ui

@ui.page('/page-2')
def page_two():
    ui.label('This is Page 2')
    ui.button('Go back to Page 1', on_click=lambda: ui.navigate.to('/'))