"""Gerar um conjunto e suas partes que aceite números decimais inteiros, letras e símbolos"""


def gerar_partes(conjunto):
    """Função para gerar as partes do conjunto"""
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

# Geração e apresentação da saída
conjunto_de_partes = gerar_partes(conjunto_original)
conjunto_de_partes_sem_virgulas = [
    [elemento.replace(",", "") for elemento in parte] for parte in conjunto_de_partes
]
conjunto_de_partes_sem_virgulas_sem_aspas = [
    [
        int(elemento.strip("'"))
        if elemento.strip("'").isdigit()
        else elemento.strip("'")
        for elemento in parte
    ]
    for parte in conjunto_de_partes_sem_virgulas
]
print("Conjunto de partes:", conjunto_de_partes_sem_virgulas_sem_aspas)
