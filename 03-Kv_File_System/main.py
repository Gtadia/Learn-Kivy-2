import kivy
from kivy.app import App

# We don't need the commeneted imports because the .kv file handles it on its own.

# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput    # text boxes
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):

    name = ObjectProperty(None)   # This is the variable from the kivy file 
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    text = ObjectProperty("Hello")

    def button_press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        self.text.text = ((f"Hello {name}, you like {pizza} pizza and your favorite favorite color is {color}"))    # Added to the "main" widget/GridLayout

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):   
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()