from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class StackLayoutEx(App):
    def build(self):
        
        layout = StackLayout()
        for i in range(20):
            btn = Button(text = str(i), width = 290 + i * 5, size_hint=(None, 0.15))
            layout.add_widget(btn)
       
        return layout


if __name__ == "__main__":
    window = StackLayoutEx()
    window.run()
