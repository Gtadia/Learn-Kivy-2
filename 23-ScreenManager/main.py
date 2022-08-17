from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 


# Define our different screens
class FirstWindow(Screen):  # inherits "Screen"
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):    # The window that the two windows are going to stay on
    pass


# Designated Our .kv design file
kv = Builder.load_file("main.kv")

"""
    # Instead of return a single window to work on, are goin going to do the following (written below)
class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()
"""

class AwesomeApp(App):
    def build(self):
        return kv       # Instead of having a main class that we reference to build our app on top of, we are going to return kivy (we're going to have multiple screens hold different aspects of our app)

if __name__ == "__main__":
    AwesomeApp().run()