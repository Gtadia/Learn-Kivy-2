from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window
from kivy.uix.slider import Slider      # If you want to use the slider in inside of the python file
from kivy.properties import ObjectProperty

Builder.load_file("slider.kv")

class MyLayout(Widget):
    
    slider_text = ObjectProperty()

    def slide_it(self, *args):
        print(args[1])      # args[0] = python object       args[1] = value 
        self.slider_text.font_size = int(5 * args[1])       # The font_size can equal a string or an int/float
        self.slider_text.text = str(args[1])


class MyApp(App):   
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run() 