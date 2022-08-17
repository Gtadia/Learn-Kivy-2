from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window
from kivy.animation import Animation    # We need to import this package if we want to use it

Builder.load_file("Kivy_File.kv")

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        # Define the Animation
        print(args)
        animate = Animation(
            background_color = (0, 1, 0, 1),     # You can change the background color as an animiation
            duration = 2,                      # The duration cna be changed (this is in seconds)
            opacity = 0.5                        # You can change the opacity here (instead of chaigning the background color)/changing the opacity also impacts everyting about the widget, including the text and images
            # Animations in the same function/instance of Animation/Animiation object is going to occur all the same time
        )

        # If you don't want all the animations to occur at the same time, you can split the animations into separate instances of Animation
        animate += Animation(
            size_hint = (0.5, 0.5),
            duration = 0.5
        )

        # The Third Animation
        animate += Animation(
            pos_hint = {"center_x": 0.1},
            duration = 1.5
        )

        # The Fourth Animation
        animate += Animation(
            pos_hint = {"center_x": 0.9, "center_y": 0.6},
            duration = 0.5
            
        )

        # Start the Animation
        animate.start(widget)

        # After the animation is finished, you can bind "animate" to a callback function
        animate.bind(on_complete = self.my_callback)

    # The Callback function
    def my_callback(self, *args):
        self.ids.my_label.text = "Wow, it ~moves~"
        print(args)     

class MyApp(App):   
    def build(self):
        Window.clearcolor = (0,0,0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run() 