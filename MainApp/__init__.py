import kivy 
kivy.require('1.11.1')
from kivy import Config
Config.set('graphics', 'multisamples', '0')
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    title = 'My Epic App'

    def build(self):
        return Label(text="Hello, world!")