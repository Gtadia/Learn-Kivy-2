import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  

# BoxLayout ==> Like a grid layout but you can only stack every widget in one column or in one row.

Builder.load_file("Random_Name.kv")

class MyBoxLayout(Widget):
    pass


class MyApp(App):   
    def build(self):
        return MyBoxLayout()


if __name__ == "__main__":
    MyApp().run()