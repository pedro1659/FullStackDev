"""Exemplo de tipos de cópias de lista, shallow e deepycopy"""
import copy

lista_num1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista_num2 = copy.deepcopy(
    lista_num1
)  # a alteração de elementos não é alterado em todas as listas
lista_num3 = copy.copy(lista_num2)  # a alteração de elementos altera em ambas as listas

lista_num1.append([10, 10, 10])
lista_num1[2][2] = 11
lista_num3[1][0] = 90
lista_num3.pop()
lista_num3.pop(0)
lista_num1.reverse()

print("Lista 1: ", lista_num1)
print("Lista 2: ", lista_num2)
print("Lista 3: ", lista_num3)
