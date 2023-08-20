"""Gerar um conjunto e suas partes que aceite números decimais inteiros, letras e alguns símbolos"""


def gerar_partes(conjunto):
    """Geração das partes do conjunto"""
    partes = [[]]
    for elementos in conjunto:
        novas_partes = []
        for parte in partes:
            novas_partes.append(parte + [elementos])
        partes.extend(novas_partes)

    return partes


# Entrada de dados
entrada = input("Entre com uma lista para ser gerado o conjunto de suas partes: ")
conjunto_original = entrada.strip("[]").split()
conjunto_de_partes = gerar_partes(conjunto_original)

# Remoção de vírgulas das partes do conjunto
conjunto_de_partes_sem_virgulas = [
    [elemento.replace(",", "") for elemento in parte] for parte in conjunto_de_partes
]

# Tratamento de elementos para números inteiros, letras e alguns símbolos
conjunto_de_partes_sem_virgulas_sem_aspas = [
    [
        int(elemento.strip("'"))
        if elemento.strip("'").isdigit()
        else elemento.strip("'")
        for elemento in parte
    ]
    for parte in conjunto_de_partes_sem_virgulas
]

# Geração e apresentação da saída
print("Conjunto de partes:", conjunto_de_partes_sem_virgulas_sem_aspas)
