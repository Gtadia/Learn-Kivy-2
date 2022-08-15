import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window

Builder.load_file("Random_Name.kv")

class MyLayout(Widget):
    
    def press(self): 
        # Create variables for our widget
        name = self.ids.textinput_in_kivy.text
        print(name)

        # Update the label
        self.ids.label_in_kivy.text = f"Hello {name}!"      # We can access all the attributes of a widget with an ID using "self.ids.<ID_name>"

        # Clear Input Box
        self.ids.textinput_in_kivy.text = ""


class MyApp(App):   
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()