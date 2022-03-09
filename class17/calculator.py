from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

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
            button.bind(on_press=self.on_button_press)
            h_layout1.add_widget(button)

        for item in group2:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            button.bind(on_press=self.on_button_press)
            h_layout2.add_widget(button)

        for item in group3:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            button.bind(on_press=self.on_button_press)
            h_layout3.add_widget(button)

        for item in group4:    
            button = Button(text=item,pos_hint={"center_x": 0.5, "center_y": 0.5},)
            button.bind(on_press=self.on_button_press)
            h_layout4.add_widget(button)    

        main_layout.add_widget(self.solution)
        main_layout.add_widget(h_layout1)
        main_layout.add_widget(h_layout2)
        main_layout.add_widget(h_layout3)
        main_layout.add_widget(h_layout4)

        equal_button = Button(text="=",pos_hint={"center_x": 0.5, "center_y": 0.5},)
        equal_button.bind(on_press=self.answer)
        main_layout.add_widget(equal_button)
        
        return main_layout

    def on_button_press(self, sender):
        current_text = self.solution.text
        button_text = sender.text

        if button_text == "C":
            #clear the text input
            self.solution.text = ""
        else:
            if current_text and (self.last_was_operator and button_text in self.operators):
                #dont do anything because we dont want 2 operators following each other
                return
            elif current_text == "" and button_text in self.operators:
                #first character or input must be a number not operator
                return
            else:
                new_text = current_text + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

        print(current_text)
        print(button_text)

    def answer(self,sender):
        text = self.solution.text
        if text:
            new_solution_text = str(eval(self.solution.text))
            self.solution.text = new_solution_text
            

if __name__ == "__main__":
    calcapp = CalculatorApp()
    calcapp.run()




