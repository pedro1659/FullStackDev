def decimal_to_binary(decimal_num):
    """
    Converte um número decimal para sua representação em binário.

    Args:
        decimal_num (int): O número na base decimal a ser convertido.

    Returns:
        str: A representação do número na base binária.
    """
    if decimal_num == 0:
        return "0"  # Se o número for zero, a representação binária também é zero

    binary = ""  # Inicializa uma string vazia para armazenar a representação binária

    while decimal_num > 0:
        remainder = decimal_num % 2  # Calcula o resto da divisão por 2
        binary = (
            str(remainder) + binary
        )  # Adiciona o dígito binário no início da string
        decimal_num //= 2  # Atualiza o número decimal dividindo por 2
    return binary


# Exemplo de uso
decimal_number = int(input("Digite um número decimal: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"O número {decimal_number} em binário é: {binary_representation}")
