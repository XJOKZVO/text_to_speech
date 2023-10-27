from flet import *

from app import App


def main (page: Page):
    page.title = "Wrvoice"
    page.theme_mode = ThemeMode.LIGHT
    #page.bgcolor = "black90"
    page.window_width = 350

    page.window_title_bar_hidden = True
    page.window_resizable = False
    # list_widgets = [Text("michael"), Text("sandy"), Text("steven")]
    # for text in list_widgets:
    #     page.add(main_app)
    main_app = App(page=page)
    page.add(main_app)

    page.update()
if '__main__' == __name__:
    app(target=main, assets_dir="assets")
