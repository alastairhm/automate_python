import yaml
from kivy.app import App
from kivy.uix.button import Button
from yaml.loader import SafeLoader

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

clip_array = []
with open("/Users/alastair.montgomery/gitrp/notes/clip.yml", "r") as f:
    clip_array = list(yaml.load_all(f, Loader=SafeLoader))
    clip_array = sum(clip_array, [])
TestApp().run()
