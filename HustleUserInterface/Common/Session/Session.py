from nicegui import ui, context
import json

class Session():

    def __init__(self) -> None:
        pass

    async def Session(self):
        await ui.run_javascript('await new Promise(resolve => setTimeout(resolve, 200));')

        js_user = await ui.run_javascript('localStorage.getItem("user")')
        if js_user and js_user != 'null':
            user = json.loads(js_user)
            context.client.storage['user'] = user

            username = user['username']
            is_admin = user['isAdmin']

            if is_admin == 1:
                admin = True
            else:
                admin = False


            userInfo = {
                'name' : username,
                'isAdmin' : admin
            }
            return userInfo

        else:
            return False


