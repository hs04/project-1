from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.result_input = TextInput(multiline=False, readonly=True, halign='right', font_size=32)
        buttons_layout = BoxLayout(orientation='vertical', spacing=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for button in buttons:
            buttons_layout.add_widget(Button(text=button, on_press=self.on_button_press))

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.result_input)
        layout.add_widget(buttons_layout)

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = 'Error'
        else:
            self.expression += str(instance.text)

        self.result_input.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
