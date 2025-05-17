from nicegui import ui
import requests

@ui.page('/')
def login_page():
    with ui.card().classes("absolute-center w-96"):
        ui.label("Login").classes("text-2xl mb-4")

        username_input = ui.input("Username").classes("w-full")
        password_input = ui.input("Password", password=True, password_toggle_button=True).classes("w-full")

        def handle_login():
            username = username_input.value
            password = password_input.value

            try:
                response = requests.post("http://localhost:8000/user-login", json={
                    "username": username,
                    "password": password,
                })

                if response.status_code == 200:
                    for i in response:
                        print(i)
                    ui.notify(response.json(), type="positive")
                else:
                    ui.notify("Login failed!", type="negative")
            except Exception as e:
                print(e)
                ui.notify(f"Error: {e}", type="negative")

        ui.button("Login", on_click=handle_login).classes("mt-4 w-full")
