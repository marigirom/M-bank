
from flet import *
import flet as ft
from financeDatabase import FinanceDatabase


def main(m_page:Page):
    m_page.theme_mode = 'light'
    m_page.window.width = 400
    m_page.window.max_width = 600
    m_page.window.frameless = True

    m_page.appbar = AppBar(
        leading= IconButton(icons.DASHBOARD),
        title = ft.Text("M_Sacco"),
        actions=[
            Row(
                controls=[
                    IconButton(icons.SEARCH,),
                    IconButton(icon=icons.DARK_MODE)
                ],
                spacing= 20,

            )
        ],
        center_title= True,
        bgcolor=colors.BLUE_GREY,
        color='#FFFFFF'


    )

    # bottom navigation
    m_page.navigation_bar= NavigationBar(
        destinations=[
            NavigationBarDestination(icon= icons.HOME, label="Home" ),
            NavigationBarDestination(icon=icons.TIPS_AND_UPDATES_OUTLINED, label="Updates"),
            NavigationBarDestination(icon=icons.EXPLORE, label="Discover"),
            NavigationBarDestination(icon=icons.PERSON, label='Account')
        ]
    )
    m_page.update()

    # functionalities to be implemented
    top_details_section = Container(
        height=100,
        content=Column(
            controls=[
                Text(f'username {FinanceDatabase.get_account_name(account_number='1237')}'),
                Text('Account Balance:: {balance here +>}'),
                Divider(color=colors.BLACK12, height=2),
                Text("My Performance :: ",text_align=TextAlign.CENTER,font_family='Comics', weight=FontWeight.BOLD),

                Row(
                    controls=[
                    TextButton('3months', ),
                    TextButton("1 year"),
                    TextButton("5 yrs"),
                    TextButton('10 yrs'),
                    TextButton('More > ')
                    ],
                    spacing=10,

                )
            ]
        )
    )
    list_modules_container = ListView(
        padding=10,
        controls=[
            ListTile(title = Text('Deposit to Sacco'), on_click=lambda e: print('attempt to deposit')),
            ListTile(title=Text('Withdraw to Mpesa')),
            ListTile(title= Text('Make Payments')),
            ListTile(title= Text("Locked saving Account")),
            ListTile(title= Text("Loans "))



        ],
        divider_thickness=1.2,
        spacing= 10,

    )
    m_page.controls.append(top_details_section)
    m_page.update()
    m_page.add(Container(
        content=list_modules_container,
        margin=margin.only(top=25, left=3),
        bgcolor=colors.WHITE70,
    ))

if __name__ == "__main__":
    app(target=main, view=AppView.FLET_APP, )