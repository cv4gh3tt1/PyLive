import flet as ft


def main(page: ft.Page):
    fav_icon = ft.Icon(
        name=ft.Icons.FAVORITE,
        color=ft.Colors.RED_500,
        size=50,
        tooltip="Favorite",
    )

    settings_icon = ft.Icon(
        name=ft.Icons.SETTINGS,
        color=ft.Colors.GREY_800,
        size=50,
        tooltip="Favorite",
    )

    page.add(
        fav_icon,
        settings_icon,
    )


ft.app(main)
