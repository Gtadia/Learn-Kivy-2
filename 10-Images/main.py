import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window
# from kivy.uix.image import Image        # We are going to work with images on kivy but if you wanted to work on images in the python file, you'll need to import this


Builder.load_file("Random_Name.kv")

class MyLayout(Widget):
    pass


class MyApp(App):   
    def build(self):
        Window.clearcolor = (1, 1, 0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()