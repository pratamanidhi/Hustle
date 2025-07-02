from nicegui import ui, context
from Business.UserManagement.UserBusiness import UserBusiness as UserBusiness


userManagement = UserBusiness()
class Button():
    def __init__(self) -> None:
        pass

    def ButtonLogin(self, username, password):
        async def handleLogin():
            try:
                result = userManagement.Login(username, password)
                print('Login result:', result)

                if result is False:
                    ui.notify("Login Failed: Invalid username or password.", type="negative")
                elif result is not None:
                    await ui.run_javascript(f'''
                        localStorage.setItem('user', JSON.stringify({{
                            username: "{result['username']}",
                            isAdmin: {str(result['isAdmin']).lower()}
                        }}));
                    ''', timeout=5.0)

                    ui.notify(f"Welcome {result['username']}", type="positive")
                    ui.navigate.to('/home')
                else:
                    ui.notify("Login Failed: Invalid username or password.", type="negative")

            except Exception as e:
                print("Login error:", e)
                ui.notify("Login failed due to server error.", type="negative")

        ui.button("Login", on_click=handleLogin).classes("mt-4 w-full")

    async def ButtonLogout(self):
        context.client.storage.clear()

        await ui.run_javascript('''localStorage.removeItem('user');''', timeout=5.0)
        ui.notify("You have been logged out", type="info")
        ui.navigate.to('/')