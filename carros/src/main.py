import flet as ft

from database import cars


def main(page: ft.Page):

    # Função para verificar se o item foi clicado
    # e alterar o estado do botão
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    # Função para mostrar a descrição do carro
    def show_car_description(e):
        car = next((car for car in cars if car["id"] == e.control.parent.key), None)
        dlg = ft.AlertDialog(
            title=ft.Text(car["descricao"]),
            actions=[
                ft.TextButton("Fechar", on_click=lambda e: page.close(dlg)),
            ],
        )
        page.open(dlg)

    # Função para deletar o carro
    # e fechar o popup
    def delete_car(e):
        e.control.parent.parent.visible = False
        page.update()

    page.title = "Vintage Cars"
    page.window.height = 600
    page.window.width = 600

    app_bar = ft.AppBar(
        # Botão de voltar "Home"
        leading=ft.IconButton(
            icon=ft.Icons.HOME,
            icon_color=ft.Colors.BLUE_GREY_100,
            tooltip="Menu",
            padding=20,
        ),
        # Título do AppBar
        leading_width=40,
        title=ft.Text(
            "Vintage Cars",
            color=ft.Colors.BLUE_GREY_50,
            weight=ft.FontWeight.BOLD,
            italic=True,
        ),
        center_title=True,
        bgcolor=ft.Colors.BLUE_GREY_900,
        # Ações do AppBar
        actions=[
            # Botão de notificações
            ft.IconButton(
                icon=ft.Icons.NOTIFICATIONS,
                icon_color=ft.Colors.BLUE_GREY_100,
                tooltip="Notificações",
            ),
            # Espaçador entre o ícone de notificações e o menu
            ft.Container(width=10),  # Ajuste a largura conforme necessário
            # Menu suspenso
            ft.PopupMenuButton(
                bgcolor=ft.Colors.BLUE_GREY_50,
                icon_color=ft.Colors.BLUE_GREY_100,
                icon=ft.Icons.MENU,
                menu_padding=10,
                tooltip="Menu",
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.PERSON,
                        text="Perfil",
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.SETTINGS,
                        text="Configurações",
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.CONTACT_MAIL,
                        text="Contato",
                    ),
                    ft.PopupMenuItem(),  # cria um Separador
                    ft.PopupMenuItem(
                        text="Mostrar todos",
                        checked=False,
                        on_click=check_item_clicked,
                    ),
                ],
            ),
            # Espaçador
            ft.Container(width=20),  # Ajuste a largura conforme necessário
        ],
    )

    # Lista de carros
    # Adicionando a lista de carros na tela
    cars_list = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
    )
    for car in cars:
        car_component = ft.ListTile(
            leading=ft.Image(
                src=car["foto"],
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                height=100,
                width=100,
                border_radius=5,
            ),
            title=ft.Text(f'{car["modelo"]} - {car["marca"]}'),
            subtitle=ft.Text(car["ano"]),
            trailing=ft.PopupMenuButton(
                key=car["id"],
                icon=ft.Icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.REMOVE_RED_EYE_SHARP,
                        text="Ver descrição",
                        on_click=show_car_description,
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.DELETE,
                        text="Deletar",
                        on_click=delete_car,
                    ),
                ],
            ),
        )
        cars_list.controls.append(car_component)

    # Adicionando a barra de navegação na parte inferior da tela
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.DIRECTIONS_CAR_FILLED_OUTLINED,
                label="Usados",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.CAR_RENTAL,
                label="Novos",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ELECTRIC_CAR,
                label="Elétricos",
            ),
        ],
    )

    page.add(
        app_bar,
        nav_bar,
        cars_list,
    )


ft.app(main)
