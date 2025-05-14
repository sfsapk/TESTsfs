from kivy.app import App
from kivy.uix.label import Label

class RocketEditorApp(App):
    def build(self):
        return Label(text='Rocket Editor')

if __name__ == '__main__':
    RocketEditorApp().run()
