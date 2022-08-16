import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window

Builder.load_file("Random_Name.kv")

class MyLayout(Widget):
    pass


class MyApp(App):   
    def build(self):
        Window.clearcolor = (1, 1, 1)       # You can LITERALLY change the background color (if you are using the "hacky" way by using a white canvas within the kivy file, then that canvas is going to be what you see because the canvas sits on top of the background)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()