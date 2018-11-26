class Start(object):
    def __init__(self):
        self.contador = 0

    def heapify(self, seq):
        for i in reversed(range(1, len(seq))):
            self.contador += 1
            parent = (i - 1) // 2

            if seq[i] > seq[parent]:
                seq[i], seq[parent] = seq[parent], seq[i]

    def sort(self, iterable):
        result = []
        seq = list(iterable)

        while seq:
            self.heapify(seq)
            result.append(seq.pop(0))

        return result
