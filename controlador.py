# coding: utf-8

# author: André Luiz Ramos Ferreira

from aleatorio import ListasRandomicas
from copy import deepcopy
from sort import *
from front.graficos import Tabela


class SortStart(object):
    def __init__(self, tamanho_das_listas=5, permitir_repetidos=False):
        medias = []
        bubble_sort = bubble.Start()
        selection_sort = selection.Start()
        insertion_sort = insertion.Insertion()
        heap_sort = heap.Start()
        merge_sort = merge.Start()
        quick_sort = quick.Start()
        bucket_sort = bucket.Start()
        count_sort = count.Start()
        radix_sort = radix.Start()
        lista_de_funcoes = [bubble_sort, selection_sort, insertion_sort, heap_sort, merge_sort, quick_sort,
                            count_sort, bucket_sort, radix_sort]

        if tamanho_das_listas == 10000:
            medias = [98150184.0, 49995000.0, 49995000.0, 50005000.0, 133616.0, 311418.0, 10000.0, 12487.0, 50050.0]

        else:
            lista = ListasRandomicas()
            lista = lista.start(50, tamanho_das_listas, permitir_repetidos)
            for i in lista_de_funcoes:
                lista_randomica = deepcopy(lista)
                list(map(i.sort, lista_randomica))
                medias.append(i.contador / len(lista))

        Tabela(medias)
