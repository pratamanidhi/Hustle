from nicegui import ui

menu_data = {
    'Signature': ['espresso', 'americano', 'latte', 'capucino' , 'a', 'b', 'c'],
    'Coffee': ['matcha', 'coklat', 'a' , 'o'],
    'Milk Base': ['matcha', 'coklat', 'a' , 'o'],
    'Tea': ['espresso', 'americano', 'latte', 'capucino' , 'a', 'b']
}

cart = []

def header():
    with ui.header().classes('bg-[#292928] text-white'):
        with ui.element('div').classes('flex justify-between items-center w-full'):
            ui.label('Hustle').classes('text-2xl font-bold ml-2')

            with ui.row().classes('gap-2'):
                ui.button('Home', on_click=lambda: ui.navigate.to('/home')).props('flat dense')
                ui.button('History', on_click=lambda: ui.navigate.to('/warehouse')).props('flat dense')
                ui.button('Report', on_click=lambda: ui.navigate.to('/report')).props('flat dense')

                def open_chart_popup():
                    subtotal = sum(item['qty'] * item['price'] for item in cart)
                    total = subtotal

                    with ui.dialog() as dialog, ui.card().classes('w-[400px]'):
                        ui.label('Menu Order').classes('text-xl font-bold')

                        for item in cart:
                            with ui.row().classes('items-center justify-between w-full'):
                                with ui.row().classes('items-center gap-2'):
                                    ui.image('https://via.placeholder.com/60').classes('w-12 h-12 rounded')
                                    with ui.column():
                                        ui.label(item['name']).classes('font-semibold')
                                        ui.label(f'x {item["qty"]}').classes('text-sm')
                                        ui.button('Notes ✎').props('flat dense text-sm').classes('text-brown-600 p-0')
                                ui.label(f"Rp.{item['price']:.2f}").classes('text-right font-medium')

                        ui.separator()

                        with ui.column().classes('w-full items-end text-right'):
                            ui.label(f"Subtotal: Rp.{subtotal:.2f}")
                            ui.label(f"Total: Rp.{total:.3f}").classes('text-lg font-bold')

                        ui.label("Payment Method").classes('mt-4 font-semibold')

                        with ui.row().classes('justify-center gap-4'):
                            ui.button('Cash').props('outline')
                            ui.button('QR').props('outline')

                        ui.button('Print Orders', on_click=lambda: print('Print...')).classes(
                            'mt-4 w-full bg-brown-600 text-white')
                        ui.button('Tutup', on_click=dialog.close).props('flat').classes('mt-2 text-gray-600')

                    dialog.open()

                ui.icon('bar_chart') \
                    .on('click', open_chart_popup) \
                    .classes('cursor-pointer text-white text-2xl hover:text-green-400')


def show_item_popup(name):
    with ui.dialog() as dialog, ui.card():
        ui.image('https://via.placeholder.com/150').classes('w-full')
        ui.label(name).classes('text-h5 font-bold')
        ui.label('Rp. 5.000')

        def tambah_ke_keranjang():
            for item in cart:
                if item['name'] == name:
                    item['qty'] += 1
                    break
            else:
                cart.append({'name': name, 'qty': 1, 'price': 5000})  # harga dummy
            dialog.close()

        ui.button('Tambah ke keranjang', on_click=tambah_ke_keranjang).classes('mt-4')
        ui.button('Tutup', on_click=dialog.close).props('flat').classes('text-gray-600')
    dialog.open()

def menu():
    with ui.splitter(value=20).classes('w-full h-screen') as splitter  :
        with splitter.before:
            with ui.tabs().props('vertical').classes('w-full text-black') as tabs:
                tab_dict = {category: ui.tab(category) for category in menu_data}
        with splitter.after:
            with ui.tab_panels(tabs, value=next(iter(tab_dict.values()))).classes('p-4'):
                for category, tab in tab_dict.items():
                    with ui.tab_panel(tab):
                        ui.label(category).classes('text-h4 mb-4')
                        with ui.grid(columns=4).classes('gap-4'):
                            for item in menu_data[category]:
                                with ui.card().classes('w-full hover:bg-gray-100 cursor-pointer') as card:
                                    ui.image('https://via.placeholder.com/100').classes('w-full')
                                    ui.label(item).classes('text-center font-medium')
                                    card.on('click', lambda e, name=item: show_item_popup(name))


header()
menu()

ui.run()