# coding: utf-8

# author: André Luiz Ramos Ferreira

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Texto(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)


class Teste(BoxLayout):
    pass


class Aplicativo(App):
    def build(self):
        return Teste()


if __name__ == '__main__':
    Aplicativo().run()
