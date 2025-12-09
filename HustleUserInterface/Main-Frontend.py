from nicegui import ui
import UserManagement.Login as Login
import Warehouse.WarehouseContent as WarehouseContent
import Home.HomeContent as HomeContent
import Menu.MenuContent as MenuContent
import Report.ReportContent as ReportContent
import Supplier.SupplierContent as SupplierContent
import PIP.PipContent as PipContent
import Test.Test

if __name__ in {"__main__", "__mp_main__"}:
    Login.Content()
    WarehouseContent.Content()
    HomeContent.Content()
    MenuContent.Content()
    ReportContent.Content()
    SupplierContent.Content()
    PipContent.Content()


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
    ui.run(reload=False, show=False, native=False, host='127.0.0.1', port=8081)
