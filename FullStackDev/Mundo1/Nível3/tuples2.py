"""Exemplo de tuples com significado"""

import collections

Pessoa = collections.namedtuple("Pessoa", "nome idade")

Joao = Pessoa(nome="João", idade=20)
print(Joao.nome, Joao.idade)
