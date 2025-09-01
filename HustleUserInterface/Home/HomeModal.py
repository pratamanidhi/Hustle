from nicegui import ui

class HomeModal():
    def __init__(self) -> None:
        pass

    def DeleteDialInModal(self, data):
        dialog = ui.dialog()

        def onDeleteConfirmation():
            ui.notify("delete success")

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):
            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            ui.label('Confirmation').classes('text-2xl font-semibold text-gray-800')
            ui.separator()
            ui.label(f"Are you sure going to delete this item?")

            ui.button('Yes', on_click=onDeleteConfirmation) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

        dialog.open()