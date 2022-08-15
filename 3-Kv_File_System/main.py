import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    # text boxes
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs): 
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1
        self.row_force_default = True
        self.row_default_height  = 120
        self.col_force_default = True
        self.col_default_height = 100 
        
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height = 40, 
            col_force_default = True, 
            col_default_width = 100
        )
        self.top_grid.cols = 2
        self.bottom_grid = GridLayout()
        self.bottom_grid.cols = 1


        self.top_grid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False,
            font_size=32,
            size_hint_y = None, 
            height = 50,
            size_hint_x = None,
            width = 400
            )
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=True)
        self.top_grid.add_widget(self.color)

        self.submit = Button(text="Submit",
            font_size=32,
            size_hint_y = None, 
            height = 50
            )
        self.submit.bind(on_press=self.button_presses_abcdefg)
        self.bottom_grid.add_widget(self.submit)

        self.add_widget(self.top_grid)
        self.add_widget(self.bottom_grid)


    def button_presses_abcdefg(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza and your favorite favorite color is {color}"))    # Added to the "main" widget/GridLayout

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()