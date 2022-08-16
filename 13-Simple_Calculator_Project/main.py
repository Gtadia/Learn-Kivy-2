from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 
from kivy.lang import Builder  
from kivy.core.window import Window

# Set the window size
Window.size = (500, 700)

Builder.load_file("calc.kv")

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    # Create function to remove last character in text box
    def backspace(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]      # Get characters from the first index to the last index but the last index in exclusive

    # Create function to make text box positive or negative
    def pos_neg(self):
        # Check if there's already a "-" sign
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'      # "replace" is a function that replaces every "-" with 
        else:
            self.ids.calc_input.text = f'-{prior}'


    def button_press(self, button):
        # create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # Check for ERROR
        if self.ids.calc_input.text == "ERROR":
            self.ids.calc_input.text = self.ids.calc_input.text[5:]

        # If the only number is 0, then just remove it because we don't want it (including when the user types 0 first (beacuse it's pointless to type 0 first))
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{button}"
        else:
            # self.ids.calc_input.text = f"{prior}{button}"   # This is able to concatenate the prior number and the current nubmer together
            self.ids.calc_input.text += f"{button}"      # or you could just do this
    
    # Math Operation function
    def math_operation(self, operation):
       self.ids.calc_input.text += operation

    # Decimal/dot function
    def dot(self):
        dot_list = self.ids.calc_input.text.split("+")  # for just addition
        if "+" in self.ids.calc_input.text and "." not in dot_list[-1]:
            self.ids.calc_input.text += "."
        elif "." in self.ids.calc_input.text:
            pass
        else:
            self.ids.calc_input.text += "."

    # Create equals function
    def equals(self):
        prior = self.ids.calc_input.text
        # error handling (just in case someone tries to divide by 0 or bring something to the infinity power)
        try:
            answer = eval(prior)        # It will take a stirng operation and convert it into an int (e.g., eval("5+5") ==> 10 )
            self.ids.calc_input.text = str(answer)
            # eval() also works with exponents (e.g., eval("2**5") = 32)
        except: 
            self.ids.calc_input.text = "ERROR"
       

class MyApp(App):   
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()