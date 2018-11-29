# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        if len(lista) > 1:
            mid = len(lista) // 2
            lefthalf = lista[:mid]
            righthalf = lista[mid:]

            self.sort(lefthalf)
            self.sort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                self.contador += 1
                if lefthalf[i] < righthalf[j]:
                    lista[k] = lefthalf[i]
                    i = i + 1
                else:
                    lista[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                self.contador += 1
                lista[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                self.contador += 1
                lista[k] = righthalf[j]
                j = j + 1
                k = k + 1

        return lista
