from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        
        main_layout = BoxLayout(orientation="vertical")
        h_layout1 = BoxLayout()
        h_layout2 = BoxLayout()
        h_layout3 = BoxLayout()
        h_layout4 = BoxLayout()

        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        
        group1 = ["7", "8", "9", "/"]
        group2 = ["4", "5", "6", "*"]
        group3 = ["1", "2", "3", "-"]
        group4 = [".", "0", "C", "+"]
       
        for item in group1:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            #button.bind(on_press=self.on_button_press)
            h_layout1.add_widget(button)

        for item in group2:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            #button.bind(on_press=self.on_button_press)
            h_layout2.add_widget(button)

        for item in group3:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            #button.bind(on_press=self.on_button_press)
            h_layout3.add_widget(button)

        for item in group4:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            #button.bind(on_press=self.on_button_press)
            h_layout4.add_widget(button)

        

        main_layout.add_widget(self.solution)
        main_layout.add_widget(h_layout1)
        main_layout.add_widget(h_layout2)
        main_layout.add_widget(h_layout3)
        main_layout.add_widget(h_layout4)

        equal_button = Button(text="=",pos_hint={"center_x": 0.5, "center_y": 0.5},)
        main_layout.add_widget(equal_button)
        
        return main_layout

if __name__ == "__main__":
    calcapp = CalculatorApp()
    calcapp.run()




