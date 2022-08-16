import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    # text boxes
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs): 
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Create the Top Gridlayout    (Beacuse we can't tell Kivy to have the button span 2 colunmns (or rows), we are going to have a gridlayout inside of a gridlayout (one for the labels an textboxes and another for the submit button))
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        
        # Create the Bottom GridLayout      (For the Submit button so we're basically only going to have 1 item in the grid)
        self.bottom_grid = GridLayout()
        self.bottom_grid.cols = 1


        # Add Widgets (to "top_grid" using "top_grid.add_widget" isntead of just "add_widget")
        self.top_grid.add_widget(Label(text="Name: "))   # You add widgets from the python file uisng "self.add_widget"
        # Add Input/Text Box
        self.name = TextInput(multiline=False)  # You can't have multiple lines in the text box
        self.top_grid.add_widget(self.name)      # You can have a widget saved as a variable and then "add_widget" that variable

        # Adding additional widgets
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # Adding even more widgets
        self.top_grid.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=True)
        self.top_grid.add_widget(self.color)

        # Create a Submit Button
        self.submit = Button(text="Submit")
        # Bind the Button (so that it has an action when it is pressed)
        self.submit.bind(on_press=self.button_presses_abcdefg)    # It doesn't really matter what it's called
        # Adding the button to the "bottom_grid"
        self.bottom_grid.add_widget(self.submit)

        # Adding both "top_grid" and "bottom_grid" to the GridLayout on MyGridLayout, which is the main window
        self.add_widget(self.top_grid)
        self.add_widget(self.bottom_grid)


    def button_presses_abcdefg(self, instance):
        # instance = When we are binding something, we what the instance of the thing that its binded to
        # Outside of the init function, we are going to create the function that contains the actions of the button press
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text     # "text" is the text that the user typed in the text boxes

        # We can print the information in the terminal
        print(f"Hello {name}, you like {pizza} pizza and your favorite favorite color is {color}")

        # Or we can just display a label that displays this information
        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza and your favorite favorite color is {color}"))    # Added to the "main" widget/GridLayout


        # Clear the input boxes after clicking the button
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()