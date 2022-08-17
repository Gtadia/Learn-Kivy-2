from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window
from kivy.animation import Animation    # We need to import this package if we want to use it

Builder.load_file("Kivy_File.kv")

class MyLayout(Widget):
    def press_it(self):
        current_value = self.ids.my_progress_bar.value
        # increment value
        current_value += 25     
        if current_value > 100:     # if current_value > 100, then go back to 0
            current_value = 0
        # update the progress bar   (and the label)
        self.ids.my_progress_bar.value = current_value
        self.ids.my_label.text = f"{current_value}% Progress"

class MyApp(App):   
    def build(self):
        Window.clearcolor = (0,0,0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run() 