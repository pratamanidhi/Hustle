from nicegui import ui

class TestContent():
    def __init__(self) -> None:
        pass


    def TestHeader(self):
        with ui.element('div').classes('grid grid-cols-3 gap-2 p-4'):
            for i, height in enumerate([50, 50, 50, 150, 100, 50]):
                tailwind = f'h-[{height}px] bg-blue-100 break-inside-avoid p-2'
                with ui.card().classes(tailwind):
                    ui.label(f'Card #{i + 1}')