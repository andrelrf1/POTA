# coding: utf-8

# author: André Luiz Ramos Ferreira


class Start(object):
    def __init__(self):
        self.contador = 0

    def sort(self, lista=[]):
        if lista:
            bins = [[], [], [], [], [], [], [], [], [], []]

            # get largest element to determine when sort is done
            m = max(lista)
            # decimal digit currently partitioning on (1,10,100...)
            r = 1

            while m > r:
                # append each element of lista to the end of the bin
                # corresponding to the partition digit
                for e in lista:
                    self.contador += 1
                    bins[int((e / r) % 10)].append(e)

                r = r * 10

                # move values from bins back to lista single list
                lista = []
                for i in range(10):
                    self.contador += 1
                    lista.extend(bins[i])
                    bins[i] = []

        return lista
