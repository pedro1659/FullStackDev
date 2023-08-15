"""Transformar entradas numericas para sua representação em binario."""


def decimal_para_binario(num_decimal):
    """Converte um número decimal para sua representação em binário."""
    if num_decimal == 0:
        return "0"  # Se o número for zero, a representação binária também é zero

    num_binario = (
        ""  # Inicializa uma string vazia para armazenar a representação binária
    )

    while num_decimal > 0:
        resto = num_decimal % 2  # Calcula o resto da divisão por 2
        num_binario = (
            str(resto) + num_binario  # Adiciona o dígito binário no início da string
        )
        num_decimal //= 2  # Atualiza o número decimal dividindo por 2
    return num_binario


n_decimal = int(input("Digite um número decimal: "))
REPRES_BINARIA = decimal_para_binario(n_decimal)
print(f"O número {n_decimal} em binário é: {REPRES_BINARIA}")
