from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=30, size_hint_y=None, height=200))


class Teste(App):
    def build(self):
        return Tarefas(["Comprar biscoito", "comprar Nescau", "Comprar Arroz", "Comprar chocolate", "Comprar bala"])


if __name__ == '__main__':
    Teste().run()
