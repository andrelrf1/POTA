# coding: utf-8

# author: André Luiz Ramos Ferreira
from controlador import SortStart


class Main(object):
    def __init__(self):
        while True:
            print("-" * 50)
            print("Comparação de desempenho entre sorts".upper().center(50))
            print("-"*50)
            print("\n1 - Tamanho 5\n2 - Tamanho 10\n3 - Tamanho 50\n4 - Tamanho 100\n5 - Tamanho 1000 (Lento)\n"
                  "6 - Tamanho 10000\n0 - Cancelar\n")
            escolha = int(input("Selecione o tamanho dos vetores: "))

            if escolha == 1:
                SortStart()

            if escolha == 2:
                SortStart(10)

            if escolha == 3:
                SortStart(50)

            if escolha == 4:
                SortStart(100)

            if escolha == 5:
                SortStart(1000)

            if escolha == 6:
                SortStart(10000)

            if escolha == 0:
                break

            else:
                continue


if __name__ == '__main__':
    Main()
