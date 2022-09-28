from collections import deque


class D:

    def __init__(self, n=10):
        self.n = n
        self.array = deque()
        self.size = 0

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return f'{self.array}'

    def first(self):
        return self.array[0]

    def ultimo_tipo(self):
        return self.array[len(self.array)-1][0]

    def pop(self):
        return self.array.pop()

    def popleft(self):
        return self.array.popleft()

    def append(self, dado):
        if self.size == self.n:
            self.array.popleft()
            self.array.append(dado)
        else:
            self.array.append(dado)
            self.size += 1

    # Funções abaixo utilizadas para acessar os indices das filas no código
    def saldo(self):
        return self.array[-1][4]

    def preco(self):
        return self.array[-1][3]
