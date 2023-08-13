# Entrada dos dados
conjunto_original = [1, 2, 3]


# Cálculos intermediários usando tabela-verdade para obter combinações
def calcular_combinacoes(conjunto):
    n = len(conjunto)
    combinacoes = []

    for i in range(1, 2**n):
        subconjunto = []
        for j in range(n):
            if (i >> j) & 1:
                subconjunto.append(conjunto[j])
        combinacoes.append(subconjunto)

    return combinacoes


combinacoes_intermediarias = calcular_combinacoes(conjunto_original)


# Função para gerar as partes do conjunto
def gerar_partes(conjunto):
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
