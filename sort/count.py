# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        valor_maximo = max(lista) + 1
        count = [0] * valor_maximo
        for a in lista:
            self.contador += 1
            count[a] += 1

        i = 0
        for a in range(valor_maximo):
            for c in range(count[a]):
                lista[i] = a
                i += 1

        return lista
