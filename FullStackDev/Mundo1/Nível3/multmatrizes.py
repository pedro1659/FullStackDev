"""Multiplicação de matrizes"""


def mult_matrizes(mat_a, mat_b):
    """Função principal"""
    num_colunas_a = len(mat_a[0])
    num_colunas_b = len(mat_b[0])

    matriz_produto = []

    for linha in range(num_colunas_a):
        matriz_produto.append([])
        for coluna in range(num_colunas_b):
            matriz_produto[linha].append(0)
            for k in range(num_colunas_a):
                matriz_produto[linha][coluna] += mat_a[linha][k] * mat_b[k][coluna]
    return matriz_produto


matriz_a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matriz_b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(mult_matrizes(matriz_a, matriz_b))
