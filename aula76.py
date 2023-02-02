# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Caroline',
    'sobrenome': 'Bento',
    'idade': 19,
    'altura': 1.67,
    'enderecos': [
        {'rua': 'aaaaaaaaaaa', 'número': 456},
        {'rua': 'desespero', 'número': 789}
    ]
}

print(pessoa)
print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])

for chave in pessoa:
    print(pessoa[chave])