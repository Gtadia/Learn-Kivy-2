import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder  

Builder.load_file("Random_Name.kv")

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