# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        numero_de_elementos = len(lista) - 1
        ordenado = False

        while not ordenado:
            ordenado = True

            for i in range(numero_de_elementos):
                self.contador += 1

                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    ordenado = False

        return lista
