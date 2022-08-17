from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window

Builder.load_file("Kivy_File.kv")

class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        print(switchValue)      # Prints "True" and "False"
        print(switchObject)     # Prints the object address name

        self.ids.my_label.text = f"The State of the Swtich: {switchValue}"
        
        if not switchValue: 
            # If the switch is off/False, then disable the switch entirely
            self.ids.my_switch.disabled = True  
        

class MyApp(App):   
    def build(self):
        Window.clearcolor = (0,0,0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run() 