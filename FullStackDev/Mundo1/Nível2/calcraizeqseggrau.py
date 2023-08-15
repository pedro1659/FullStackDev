"""
Calculadora de Equações Quadráticas

Calcula as raízes de uma equação quadrática com base nos coeficientes inseridos pelo usuário.
"""

from ast import literal_eval
import numpy as np


def obter_coeficiente():
    """Obtém o valor do coeficiente inserido pelo usuário."""
    coeficiente = literal_eval(input("Digite o valor do coeficiente: "))
    return coeficiente


def calcular_delta(coef_a, coef_b, coef_c):
    """Calcula o Delta para a equação quadrática."""
    return nova_funcao(coef_a, coef_b, coef_c)


def nova_funcao(coef_a, coef_b, coef_c):
    """Calcula o discriminante da equação quadrática."""
    return coef_b * coef_b - 4 * coef_a * coef_c


def calcular_raizes(coef_a, coef_b, discriminante):
    """Calcula as raízes da equação quadrática."""
    if discriminante < 0:
        return "A equação não possui raízes nos números reais."
    if discriminante == 0:
        raiz = -coef_b / (2 * coef_a)
        return f"A equação possui apenas uma raiz: {raiz}"
    raiz1 = (-coef_b - np.sqrt(discriminante)) / (2 * coef_a)
    raiz2 = (-coef_b + np.sqrt(discriminante)) / (2 * coef_a)
    return f"A equação possui as raízes: {raiz1}, {raiz2}"


# f(x) = ax^2 + bx + c
a = obter_coeficiente()
b = obter_coeficiente()
c = obter_coeficiente()

delta = calcular_delta(a, b, c)
print(calcular_raizes(a, b, delta))
