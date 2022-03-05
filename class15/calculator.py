from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
 
class CalculatorApp(App):
    def build(self):
 
        main_layout = BoxLayout(orientation="vertical")
        h_layout1 = GridLayout(cols=2)       
  
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
         
        group1 = ["7", "8", "9", "/","4", "5", "6", "*","1", "2", "3", "-",".", "0", "C", "+"]
        
        for item in group1:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            #button.bind(on_press=self.on_button_press)
            h_layout1.add_widget(button)
         
        
        main_layout.add_widget(self.solution)
        main_layout.add_widget(h_layout1)       

        equal_button = Button(text="=",pos_hint={"center_x": 0.5, "center_y": 0.5},)
        main_layout.add_widget(equal_button)
        
        return main_layout

if __name__ == "__main__":
    calcapp = CalculatorApp()
    calcapp.run()




