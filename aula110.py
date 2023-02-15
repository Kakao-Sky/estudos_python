# groupby - agrupando valores (itertools)

from itertools import groupby

# alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c', 'd']
# grupos = groupby(alunos)

# # groupby gera um iterável que tem uma chave, que referencia um grupo
# # e esse grupo é um outro iterável, que precisa de uma lista pra ser acessado 
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))
# print()

# # o groupby necessita que os valores estejam ordenados
# alunos = ['a', 'a', 'a', 'a', 'a', 'b', 'c', 'd', 'a']
# grupos = groupby(alunos)
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))
# print()


# grupos = groupby(sorted(alunos))
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))
# print()


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Quero ordenar a lista com base na nota
# -> ordena as notas, e com base nelas, ordena todos os dicionários

# sorted() sempre precisa de uma key, que vai informar como/pelo quê a ordenação será feita

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
# for aluno in alunos_agrupados:
#     print(aluno)

grupos = groupby(alunos_agrupados, key=ordena)
for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
print() 

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
print() 