# coding: utf-8

# author: André Luiz Ramos Ferreira

from aleatorio import ListasRandomicas
from copy import deepcopy
from sort import *
from tabela import Tabela


class SortMain(object):

    medias = []
    bubble_sort = bubble.Start()
    selection_sort = selection.Start()
    insertion_sort = insertion.Start()
    heap_sort = heap.Start()
    lista_de_funcoes = [bubble_sort, selection_sort, insertion_sort, heap_sort]
    lista = ListasRandomicas()
    lista = lista.start(50, 5)
    for i in lista_de_funcoes:
        lista_randomica = deepcopy(lista)
        list(map(i.sort, lista_randomica))
        print("Número de iterações: %i\nMédia: %.1f" % (i.contador, i.contador / len(lista)))
        medias.append(i.contador / len(lista))
    Tabela(medias)


if __name__ == "__main__":
    SortMain()
