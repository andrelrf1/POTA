# coding: utf-8

# author: André Luiz Ramos Ferreira
from aleatorio import ListasRandomicas


class ReadWrite(ListasRandomicas):
    def __init__(self):
        super().__init__()
        arquivo = open('lista.txt', 'w')
        lista = self.start(quantidade_de_listas=50, tamanho_das_listas=10000)
        arquivo.write(str(lista))
        arquivo.close()
        print("Lista armazenada!")


if __name__ == '__main__':
    ReadWrite()
