from nicegui import ui
from Business.UserManagement.UserBusiness import UserBusiness as UserBusiness

userBusiness = UserBusiness()

class UserManagementModal:
    def __init__(self) -> None:
        pass

    def AddUserModal(self):

        def onAddUser():
            data = {
                "username" : username.value,
                "password" : password.value,
                "isAdmin" : checkbox.value
            }

            result = userBusiness.AddUser(data)
            if result:
                ui.notify("Success to add new user")
                ui.navigate.to("/usermanagement")
                dialog.close()
            else:
                ui.notify("Failed to add new user")

        dialog = ui.dialog()

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):

            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            ui.label('User Management Form').classes('text-2xl font-semibold text-gray-800')
            ui.separator()

            with ui.column().classes('relative p-4 border rounded-md'):
                with ui.grid(columns=2).classes('gap-3'):
                    ui.label('Username')
                    username = ui.input(label='Username') \
                        .props('dense outlined') \
                        .classes('w-60 text-sm')

                    ui.label('Password')
                    password = ui.input(label='Password') \
                        .props('dense outlined') \
                        .classes('w-60 text-sm')

                    checkbox = ui.checkbox('Set as Admin?')

                    admin_chip = ui.chip(
                        icon='account_circle',
                        color='red-5',
                        removable=False
                    )

                    admin_chip.style('color: white; padding-left: 8px; gap: 0.5rem')
                    admin_chip.set_text('Admin')

                    admin_chip.bind_visibility_from(checkbox, 'value')

            ui.button('Add product', on_click=onAddUser) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')
        dialog.open()

    def ConfirmationDeleteModal(self, datas):
        dialog = ui.dialog()

        def onDeleteConfirmation():
            result = userBusiness.DeleteUser(datas['userId'])
            if result:
                ui.notify(f"Success to delete user of {datas['username']}")
                ui.navigate.to("/usermanagement")
                dialog.close()
            else:
                ui.notify("Failed to delete user")

        with dialog, ui.card().classes('w-full max-w-screen-md p-6 relative space-y-4 shadow-xl'):
            ui.button(icon='close', on_click=dialog.close) \
                .props('flat round dense color=grey') \
                .classes('absolute top-2 right-2 z-10')

            ui.label('Confirmation').classes('text-2xl font-semibold text-gray-800')
            ui.separator()
            ui.label(f"Are you sure going to delete account with name {datas['username']}?")


            ui.button('Yes', on_click=onDeleteConfirmation) \
                .classes('text-sm px-3 py-1 rounded-md') \
                .props('color=amber-500 text-black')

        dialog.open()

