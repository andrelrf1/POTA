import numpy as np
import matplotlib.pyplot as plt


class Tabela(object):
    def __init__(self, media=None):
        self.__media = media
        self.gerar_tabela()

    def gerar_tabela(self):
        legenda = ["Bubble", "Selection", "Insertion", "Heap", "Merge", "Quick", "Count", "Bucket", "Radix"]
        posicao = np.arange(len(self.__media))
        plt.rcParams['figure.figsize'] = (11, 7)
        plt.title("Sorts")
        plt.ylabel("Média de iterações")
        plt.xticks(posicao, legenda)
        barra = plt.bar(range(len(self.__media)), self.__media, width=0.5, alpha=0.5, color="blue")
        self.autolabel(barra)
        plt.show()

    def autolabel(self, rects, xpos='center'):
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height, '{}'.format(height),
                     ha=ha[xpos], va='bottom')
