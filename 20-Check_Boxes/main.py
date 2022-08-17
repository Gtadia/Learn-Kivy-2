from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window

Builder.load_file("Kivy_File.kv")

class MyLayout(Widget):
    checks = []         # We are going to save (and remove) any variables that are checked (or unchecked) 

    def checkbox_click(self, instance, value, topping):
        print(value)        # value is return true when clicked and false when unclicked
        print(instance)     # We can see that the instance just returns 

        if value == True:
            MyLayout.checks.append(topping)         # "MyLayout.<stuff>" is the same as "self.<stuff>"
        else: 
            MyLayout.checks.remove(topping)

        # Convert the list into a string that looks nicer
        try:
            str_checks = ''     # clear the string
            for i in range(len(MyLayout.checks) - 1):
                str_checks += f"{MyLayout.checks[i]}, "
            if len(MyLayout.checks) == 1:
                str_checks += f"{MyLayout.checks[0]}"
            else:
                str_checks += f"and {MyLayout.checks[-1]}"     # throws an error when everything is unchecked
        except:
            pass

        self.ids.output_label.text = f"You've selected: {str_checks}"


class MyApp(App):   
    def build(self):
        Window.clearcolor = (1,1,1)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run() 