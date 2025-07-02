from nicegui import ui
import UserManagement.Login
import Warehouse.WarehouseContent
import Home.HomeContent
import Menu.MenuContent
import Test.Test

if __name__ in {"__main__", "__mp_main__"}:
    ui.add_head_html('''
    <script>
        window.send_event = (name, detail) => {
            if (window.dispatch_event !== undefined) {
                window.dispatch_event(name, detail);
            } else {
                window.dispatchEvent(new CustomEvent(name, { detail }));
            }
        };
    </script>
    ''')
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    ''')
    ui.run(reload=False, show=False, native=False, host='0.0.0.0', port=8081)
