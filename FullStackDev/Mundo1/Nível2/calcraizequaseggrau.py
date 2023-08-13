import numpy as np


def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente


def calc_delta(a, b, c):
    return new_func(a, b, c)


def new_func(a, b, c):
    return b * b - 4 * a * c


def calcular_raizes(a, b, c, delta):
    if delta < 0:
        return "a equação não possui raízes nos números rais"
    elif delta == 0:
        x = -b / 2 * a
        return f"a equação possui apenas uma raiz: {x}"
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        return f"a equação possui as raízes: {x1}, {x2}"


# f(x)=ax^2+bx+c
a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta=calc_delta(a,b,c)
print(calcular_raizes(a, b, c, delta))