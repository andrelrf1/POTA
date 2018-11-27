import matplotlib.pyplot as plt
import numpy as np


class Tabela(object):
    def __init__(self, lista_de_medias=[]):
        y_axis = lista_de_medias
        x_axis = range(len(y_axis))
        width_n = 0.4  # largura das barras
        bar_color = 'grey'
        popPos = np.arange(len(lista_de_medias))
        print(lista_de_medias)

        plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
        plt.xticks(popPos, ["Bubble Sort", "Selection Sort", "Insertion Sort", "Heap Sort"])
        plt.title("Sorts")
        plt.show()
