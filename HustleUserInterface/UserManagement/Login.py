from nicegui import ui, context
from HustleUserInterface.API.UserManagement.UserManagementAPI import UserManagementAPI as User
import asyncio

@ui.page('/')
def login_page():
    with ui.card().classes("absolute-center w-96"):
        context.client.storage.clear(),
        ui.label("Login").classes("text-2xl mb-4")

        username_input = ui.input("Username").classes("w-full")
        password_input = ui.input("Password", password=True, password_toggle_button=True).classes("w-full")

        async def handle_login():
            username = username_input.value
            password = password_input.value

            result = User().Login(username, password)

            if result is not None:

                if result is False:
                    ui.notify("Login Failed: Invalid username or password.", type="negative")
                else:
                    await ui.run_javascript(f'''
                        localStorage.setItem('user', JSON.stringify({{
                            username: "{result['username']}",
                            isAdmin: {str(result['isAdmin']).lower()}
                        }}));
                    ''', timeout=5.0)

                    ui.notify(f"Welcome {result['username']}", type="positive")
                    ui.navigate.to('/warehouse')

            else:
                ui.notify("Login Failed: Invalid username or password.", type="negative")

        ui.button("Login", on_click=handle_login).classes("mt-4 w-full")
