import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
import re

Window.size = (500, 700)
Builder.load_file('calc_style.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def calculate(self):
        self.ids.calc_input.text = f"{eval(self.ids.calc_input.text)}"

    def press_button(self, button):
        query = self.ids.calc_input.text
        if query == "0":
            self.ids.calc_input.text = str(button)
        else:
            self.ids.calc_input.text = f"{query}{button}"

    def press_dot(self):
        query = self.ids.calc_input.text
        if "." not in query:
            self.ids.calc_input.text = f"{query}."
        else:
            pam = re.split("[-+/*]", query)
            if "." not in pam[-1]:
                self.ids.calc_input.text = f"{query}."

    def delete(self):
        query = self.ids.calc_input.text
        if query == "0" or len(query) == 1:
            self.ids.calc_input.text = "0"
        else:
            self.ids.calc_input.text = query[:-1]

    def operate(self, code):
        query = self.ids.calc_input.text.split(code)
        if len(query) > 1:
            self.ids.calc_input.text = f"{eval(self.ids.calc_input.text)}{code}"
        else:
            self.ids.calc_input.text = f"{self.ids.calc_input.text}{code}"

    def negate(self):
        query = self.ids.calc_input.text
        text = eval(query) * -1
        self.ids.calc_input.text = str(text)


class CalculatorApp(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()