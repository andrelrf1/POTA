# coding: utf-8

# author: André Luiz Ramos Ferreira
from sort.insertion import Insertion


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        insertion_sort = Insertion()
        largest = max(lista)
        length = len(lista)
        size = largest / length

        buckets = [[] for _ in range(length)]
        for i in range(length):
            j = int(lista[i] / size)
            if j != length:
                self.contador += 1
                buckets[j].append(lista[i])
            else:
                buckets[length - 1].append(lista[i])

        for i in range(length):
            insertion_sort.sort(buckets[i])

        self.contador += insertion_sort.contador
        result = []
        for i in range(length):
            result = result + buckets[i]

        return result
