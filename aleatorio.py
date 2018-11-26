# coding: utf-8

# author: André Luiz Ramos Ferreira

import random


class ListasRandomicas(object):
    def start(self, quantidade_de_listas=0, tamanho_das_listas=0):
        lista_de_itens = []

        for i in range(quantidade_de_listas):
            lista = []

            while len(lista) < tamanho_das_listas:
                valor = random.randrange(20000)

                if valor not in lista:
                    lista.append(valor)

            lista_de_itens.append(lista)

        return lista_de_itens
