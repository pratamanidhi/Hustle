from nicegui import ui
from datetime import datetime
from UserManagement.UserManagementModal import UserManagementModal as UserManagementModal

modal = UserManagementModal()

class UserManagementLayout:
    def __init__(self) -> None:
        pass

    def UserManagementContent(self, userList):
        def addNewUser():
            modal.AddUserModal()


        ui.button('Add new user', on_click=addNewUser) \
            .props('flat dense')
        ui.separator()
        ui.label("List of user").classes('font-semibold text-gray-800')
        with ui.grid().classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 w-full'):
            for user in userList:
                with ui.card().classes('p-0 shadow-sm !border-0 w-full'):
                    self.UserList(user)

    def UserList(self, user):
        def onDeleteUser():
            modal.ConfirmationDeleteModal(user)

        with ui.column().classes('w-full relative p-4 border-2 rounded-3xl'):
            if (user["isAdmin"] == True):
                ui.chip(icon='account_circle', color='red-5', removable=False).style(
                    'color: white; padding-left: 8px; gap: 0.5rem').set_text("Admin")
            else:
                ui.chip(icon='account_circle', color='indigo-5', removable=False).style(
                    'color: white; padding-left: 8px; gap: 0.5rem').set_text("Common User")
            with ui.column().classes('w-full p-4 border-2 rounded-3xl h-full'):
                with ui.grid(columns=2).classes('gap-5'):
                    ui.label("Name").classes('font-semibold text-gray-800')
                    ui.label(user["username"])

                    ui.label("Password").classes('font-semibold text-gray-800')
                    ui.label(user["password"])

                    ui.label("Last Login").classes('font-semibold text-gray-800')
                    if user["lastLogin"] is not None:
                        dt = datetime.fromisoformat(str(user["lastLogin"]))
                        formatted_date = dt.strftime("%Y %b %d %H:%M:%S")
                        ui.chip(icon='calendar_today', color='indigo-5', removable=False).style(
                            'color: white; padding-left: 8px; gap: 0.5rem').set_text(formatted_date)
                    else:
                        ui.label("-")

                    ui.label("Last Logout").classes('font-semibold text-gray-800')
                    if user["lastLogout"] is not None:
                        dt = datetime.fromisoformat(str(user["lastLogout"]))
                        formatted_date = dt.strftime("%Y %b %d %H:%M:%S")
                        ui.chip(icon='calendar_today', color='indigo-5', removable=False).style(
                            'color: white; padding-left: 8px; gap: 0.5rem').set_text(formatted_date)
                    else:
                        ui.label("-")


            ui.button('Delete', on_click=onDeleteUser) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

