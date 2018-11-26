# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        for i in range(len(lista) - 1):
            valor_menor = i

            for j in range(i + 1, len(lista)):
                self.contador += 1

                if lista[j] < lista[valor_menor]:
                    valor_menor = j

            lista[i], lista[valor_menor] = lista[valor_menor], lista[i]

        return lista
