from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatLayoutEx(App):
    def build(self):

        layout = FloatLayout(size=(200, 300))
        button = Button(text='Hello world', size_hint=(.5, .25),  pos=(60, 80))
        button1 = Button(text='Hello world 2', size_hint=(.5, .25),  pos=(120, 160))

        layout.add_widget(button)
        layout.add_widget(button1)
        return layout      



if __name__ == "__main__":
    window = FloatLayoutEx()
    window.run()
