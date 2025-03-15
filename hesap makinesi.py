import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

kivy.require('2.0.0')  # Kivy sürümünü belirtiyoruz.

class CalculatorApp(App):
    def build(self):
        self.result = TextInput(font_size=32, halign='right', multiline=False)
        self.result.text = '0'

        layout = GridLayout(cols=4, padding=10, spacing=10)

        # Hesap makinesi butonlarını tanımlıyoruz
        buttons = [
            ('7', self.append_number), ('8', self.append_number), ('9', self.append_number), ('/', self.append_number),
            ('4', self.append_number), ('5', self.append_number), ('6', self.append_number), ('*', self.append_number),
            ('1', self.append_number), ('2', self.append_number), ('3', self.append_number), ('-', self.append_number),
            ('C', self.clear), ('0', self.append_number), ('=', self.calculate), ('+', self.append_number)
        ]

        # Butonları ekliyoruz
        for (text, callback) in buttons:
            button = Button(text=text, on_press=callback)
            layout.add_widget(button)

        layout.add_widget(self.result)
        return layout

    def append_number(self, instance):
        current_text = self.result.text
        if current_text == '0':
            self.result.text = instance.text
        else:
            self.result.text += instance.text

    def clear(self, instance):
        self.result.text = '0'

    def calculate(self, instance):
        try:
            # Hesaplamayı yapıyoruz
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = 'Error'

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
