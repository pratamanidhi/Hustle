from nicegui import ui
from HustleUserInterface.API.UserManagement.UserManagementAPI import UserManagementAPI as User
import asyncio

@ui.page('/login')
def login_page():
    with ui.card().classes("absolute-center w-96"):
        ui.label("Login").classes("text-2xl mb-4")

        username_input = ui.input("Username").classes("w-full")
        password_input = ui.input("Password", password=True, password_toggle_button=True).classes("w-full")

        spinner = ui.spinner().style('display:none')  # hidden initially

        def handle_login():
            spinner.style('display:block')  # show spinner
            username = username_input.value
            password = password_input.value

            result = User().Login(username, password)
            spinner.style('display:none')  # hide spinner

            if result is not None:
                ui.notify("Login Success", type="positive")
                ui.navigate.to('/warehouse')
            else:
                ui.notify("Login Failed: Invalid username or password.", type="negative")

        ui.button("Login", on_click=handle_login).classes("mt-4 w-full")