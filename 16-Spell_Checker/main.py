from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder  
from kivy.core.window import Window
# from kivy.core.spelling import Spelling    # Kivy comes with a package that has spell checking abilities
import enchant

"""
In order for "Spelling" to work, you need to have pyenchant (but with ARM based macs (such a the M1), I need to
download the intel mac version of pyenchant)
"""

Builder.load_file("my_kivy_file.kv")

class MyLayout(Widget):
    def press(self):
        # Create instance of Spelling
        # s = Spelling()

        # Select the language
        # s = enchant.request_dict("en_US")
        s = enchant.Dict('en_US')

        word = self.ids.word_input.text

        option = s.suggest(word)

        # self.ids.word_label.text = str(option)


class MyApp(App):   
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run() 