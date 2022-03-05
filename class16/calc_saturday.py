from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        h_layout1 = GridLayout(cols=4)        

        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        
        group1 = ["7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        ".", "0", "C", "+"]        
       
        for item in group1:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            button.bind(on_press=self.on_button_press)
            h_layout1.add_widget(button)
                
        main_layout.add_widget(self.solution)
        main_layout.add_widget(h_layout1)

        clearlast_button = Button(text="CE",pos_hint={"center_x": 0.5, "center_y": 0.5},)
        #clearlast_button.bind(on_press=self.xxxxxxxxxxx)
        main_layout.add_widget(clearlast_button)

        equal_button = Button(text="=",pos_hint={"center_x": 0.5, "center_y": 0.5},)
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)
        
        return main_layout

    def on_button_press(self, instance):        
        current = self.solution.text
        button_text = instance.text
    
        if button_text =="C":
            #clear the solution text input
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                #dont permit 2 operators to follow each other
                return
            elif current =="" and  button_text in self.operators:
                #the first button should not be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators
    
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    calcapp = CalculatorApp()
    calcapp.run()
