import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder   # We can use the builder to load cetain kivy files (so you can name the kivy file anything you want and not worry about matching the name)

# This is the first way to designate a certain kivy file to a certain python file
Builder.load_file("Random_Name.kv")

# This is the second way to designate a certain kivy file to this python file (A string loading method — writing out your entire kivy file inside of the multiline string
# Builder.load_string("""
# <MyGridLayout>
#     name:name_for_kv
#     pizza:pizza_for_kv
#     color:color_for_kv
#     text:text_for_kv

#     GridLayout:
#         cols: 1
#         size: root.width, root.height
#         GridLayout: 
#             cols: 2

#             Label: 
#                 text: "Name"
#             TextInput:
#                 id: name_for_kv
#                 multiline: False

#             Label: 
#                 text: "Favorite Pizza"
#             TextInput:
#                 id: pizza_for_kv
#                 multiline: False

#             Label: 
#                 text: "Favorite Color"
#             TextInput:
#                 id: color_for_kv 
#                 multiline: False            
        
#         Button:
#             text: "Submit"
#             font_size: 72
#             on_press: root.button_press()
        
#         Label:
#             id: text_for_kv
# """)

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    text = ObjectProperty("Hello")

    def button_press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        self.text.text = ((f"Hello {name}, you like {pizza} pizza and your favorite favorite color is {color}"))

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):   
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()