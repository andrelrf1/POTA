# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        for i in range(1, len(lista)):
            for j in range(i, 0, -1):
                self.contador += 1

                if lista[j - 1] > lista[j]:
                    lista[j - 1], lista[j] = lista[j], lista[j - 1]

        return lista
