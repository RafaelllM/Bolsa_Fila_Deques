class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self) -> str:
        return f'{self.items}'

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def append(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# Funções abaixo utilizadas para acessar os indices das filas no código

    def quantidade_venda(self):
        return self.items[0][1]

    def decrescer_quantidade_compra(self):
        self.items[-1][1] -= 1

    def verificar_quantidade_compra(self) -> bool:
        return self.items[-1][1] == 0

    def valor_venda(self):
        return self.items[0][3]

    def valor_compra(self):
        return self.items[-1][3]

    def saldo(self):
        return self.items[0][1] * self.items[0][3]

    def comprar_preco_penultimo(self):
        return self.items[len(self.items)-2][3]
