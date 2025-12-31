from nicegui import ui

from Home.HomeContent import userBusiness
from Common.Session.Session import Session as Session
from Common.Layout.Layout import Layout as Layout
from Business.UserManagement.UserBusiness import UserBusiness as UserBusiness
from UserManagement.UserManagementLayout import UserManagementLayout as UserManagementLayout

userBusiness = UserBusiness()
session = Session()
layout = Layout()
userManagementLayout = UserManagementLayout()

def UserList():
    result = userBusiness.GetAlluser()
    userManagementLayout.UserManagementContent(result)

def Content():
    @ui.page('/usermanagement')
    def UserManagementContent():
        with ui.row().classes('w-full h-screen items-center justify-center') as container:
            ui.label('Loading Data..')
            ui.spinner('dots', size='lg', color='red')

        async def Init():
            result = await session.Session()

            if result is not False:
                print("user", result)
                layout.Header(result)
                UserList()
                container.visible = False
            else:
                ui.notify("No login info found", type='warning')
                ui.navigate.to('/')
        ui.timer(0.1, Init, once=True)
