# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        esquerda = []
        direita = []
        if lista:
            for i in lista:
                self.contador += 1
                if i < lista[0]:
                    esquerda.append(i)

            for j in lista:
                self.contador += 1
                if j > lista[0]:
                    direita.append(j)

            if len(esquerda) > 1:
                esquerda = self.sort(esquerda)

            if len(direita) > 1:
                direita = self.sort(direita)

            return esquerda + [lista[0]] * lista.count(lista[0]) + direita

        return []
