from collections import deque
from copy import *
from fila import *
from deque import *

# Declarando as Estruturas de dados
temp = D()  # deque
compra = Queue()  # fila
venda = Queue()  # fila

entrada = ''
numero_compras = 0

saldo = int(input('digite seu saldo: '))
primeiro_saldo = saldo

# começo do While
while entrada.lower() != 'acabou':
    entrada = input().strip(' ')

    if entrada.lower() == 'acabou':
        break

    # Retroceder
    elif entrada == '<':
        if temp.ultimo_tipo() == 'compra':  # Se a ultima operação tiver sido de compra:
            if len(temp) == 1:
                saldo = primeiro_saldo
            else:
                saldo = temp.saldo()  # trazendo o saldo de volta
            compra.pop()
            temp.pop()
            print(
                f'Retrocesso feito com sucesso!!! \nSaldo atual = R${saldo}')
        else:  # Caso a ultima operação tiver sido de venda
            saldo = temp.saldo()
            temp.pop()
            if numero_compras == len(compra):
                # Se o número de compras tiver sido igual ao de itens da lista quer dizer que
                # foram vendidas menos ações doq compradas, por isso vou retirar a ação que sobrou pra repor tudo
                compra.dequeue()
            compra.append(temp.first())
            print(
                f'Retrocesso feito com sucesso!!! \nSaldo atual = R${saldo}')

    else:
        # recebendo a entrada de compra e venda de ações
        if entrada.split(' ')[0].lower() == 'venda' and compra.size() == 0:
            raise Exception('Você não tem ações para vender')
        elif entrada.split(' ')[0].lower() == 'compra' and int(entrada.split(' ')[1]) * int(entrada.split(' ')[4]) > saldo:
            raise Exception('Saldo insuficiente para compra')
        else:
            # Criando uma lista com os dados da entrada
            dia = [entrada.split(' ')[0].lower(), int(entrada.split(' ')[
                1]), entrada.split(' ')[3].lower(), int(entrada.split(' ')[4]), saldo]
            temp.append(dia)

            if entrada.split(' ')[0].lower() == 'compra':
                numero_compras += 1
                # Estava havendo problema de shallow copy da variavel por isso importei o deepcopy
                d = deepcopy(dia)
                compra.enqueue(d)
                print(
                    f'Você gastou: R${compra.saldo()}')
                print(
                    f'Saldo atual = R${-(compra.saldo()) + saldo}')
                saldo -= (compra.saldo())

            else:
                # Estava havendo problema de shallow copy da variavel por isso importei o deepcopy
                c = deepcopy(dia)
                venda.enqueue(c)
                ganho_perda = 0
                comparativo = 0
                # Pro número de vendas vai decrescer da quantidade de ações compradas e somar com o valor
                # de venda, quando o número de ações compradas chegar a 0 tira da fila
                for i in range(venda.quantidade_venda()):
                    compra.decrescer_quantidade_compra()
                    comparativo += compra.valor_compra()
                    if compra.verificar_quantidade_compra():
                        compra.dequeue()
                    ganho_perda += venda.valor_venda()
                saldo += ganho_perda
                print(
                    f'Você comprou essas ações por R${comparativo} e as vendeu por R${ganho_perda}')
                print(
                    f'Obtendo um lucro relativo foi de {ganho_perda - comparativo}')
                print(f'Seu saldo atual é R${saldo}')
