"""Entrada dos dados"""
conjunto_original = [1, 2, 3]

def calcular_combinacoes(conjunto):
    """Cálculos intermediários usando tabela-verdade para obter combinações"""
    num_elementos = len(conjunto)
    combinacoes = []

    for i in range(1, 2 ** num_elementos):
        subconjunto = []
        for j in range(num_elementos):
            if (i >> j) & 1:
                subconjunto.append(conjunto[j])
        combinacoes.append(subconjunto)

    return combinacoes

combinacoes_intermediarias = calcular_combinacoes(conjunto_original)

def gerar_partes(conjunto):
    """Função para gerar as partes do conjunto"""
    partes = [[]]
    for elemento in conjunto:
        novas_partes = []
        for parte in partes:
            novas_partes.append(parte + [elemento])
        partes.extend(novas_partes)

    return partes

conjunto_de_partes = gerar_partes(conjunto_original)

# Apresentação dos resultados
print("A lista produzida é igual a:", conjunto_de_partes)
