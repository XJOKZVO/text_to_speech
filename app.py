from flet import *
from speech import speech

class App(UserControl):
    text_area :TextField
    list_genders :list[str]
    list_speeds :list[str]
    drop_genders = None
    drop_speeds = None
    speed_index :int
    gender_index :int
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.text_area = None
        self.list_genders = ["Male","Female"]
        self.list_speeds = ["Slow","Normal","Fast"]
        self.page.floating_action_button = FloatingActionButton(
            icon=icons.PLAY_ARROW,
            bgcolor="blue",
            on_click= self.convert
        )
        self.speed_index = 1
        self.gender_index = 0
    def convert(self,e):
        speech().convert(
            self.text_area.value,
            self.speed_index,
            self.gender_index,
        )

    def close_app(self,e):
        self.page.window_close()

    def select_gender(self,e):
        match (self.drop_genders.value):
            case "Male" : self.gender_index = 0
            case "Female" : self.gender_index = 1

    def select_speed(self,e):
        match (self.drop_speeds.value):
            case "Slow" : self.speed_index = 0
            case "Normal" : self.speed_index = 1
            case "Fast" : self.speed_index = 2

    def build(self):
        self.text_area = TextField(
                            hint_text="Enter Text",
                            expand= True,
                            min_lines=12,
                            max_lines=18,
                            text_style=TextStyle(
                                size=20
                            )
                        )
        self.drop_genders = Dropdown(
                                hint_text="Gender",
                                text_style=TextStyle(
                                size=18,
                                color="black"
                                ),
                                options=list(map(
                                    lambda item : dropdown.Option
                                    (item),
                                    self.list_genders
                                )),
                                on_change=self.select_gender
                            )
        self.drop_speeds = Dropdown(
                                hint_text="Speed",
                                text_style=TextStyle(
                                size=18,
                                color="black"
                                ),
                                options=list(map(
                                    lambda item : dropdown.Option
                                    (item),
                                    self.list_speeds
                                )),
                                on_change=self.select_speed
                            )
        return WindowDragArea(
            Column(
            # horizontal_alignment= CrossAxisAlignment.STRETCH,
            [
                Row(
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Text("Welcome", size=20, color=colors.BLUE),
                        IconButton(
                            icon=icons.CLOSE,
                            bgcolor=colors.RED,
                            icon_color="white",
                            on_click=self.close_app
                        )
                    ]
                ),
                Row(
                    [
                        Container(
                            width=150,
                            padding=20,
                            content=self.drop_genders
                        ),
                        Container(
                            width=150,
                            padding=20,
                            content=self.drop_speeds
                        )
                    ]
                ),
                Row(
                    [
                        self.text_area
                    ]
                )
            ]
        )
        )
