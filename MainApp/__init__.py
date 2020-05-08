from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    title = 'My Epic App'

    def build(self):
        return Label(text="Hello, world!")