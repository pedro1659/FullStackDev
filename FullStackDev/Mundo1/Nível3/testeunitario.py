"""Para ilustrar, vamos realizar um teste unitário para a função sum (soma) do Python."""

# Criar uma lista com os números 5, 10 e 20;
# Executar a função sum utilizando a lista criada como argumento;
# Verificar se o resultado da soma é 35, que é a soma de todos os itens da lista (esperado sucesso);
# Verificar se o resultado da soma é diferente de 35 (esperado erro)."""

lista = [5, 10, 20]
soma = sum(lista)
assert soma == 35, "Aguardando sucesso!"
assert soma != 35, "Aguardando erro!"
