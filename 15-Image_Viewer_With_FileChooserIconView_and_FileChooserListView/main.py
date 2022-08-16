from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window

Builder.load_file("my_kivy_file.kv")

class MyLayout(Widget):
    def my_selected(self, filename):
        # This is a file that has been selected from the kivy gui
        try:
            self.ids.my_image.source = filename[0]
        except:
            print("It didn't work")

class MyApp(App):   
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()