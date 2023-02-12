# Função lambda em Python
# A função Lambda é uma função como qualquer outra, mas é uma função anônima 
# que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
# Não é uma função nomeada

# lista = [1, 5, 56, 42, 50, 12, 38, 8, 8, 24, 21]
# print(lista)

# funciona para números e letras, não funciona para dict
"""lista.sort() # altera a lista original, deixa ela ordenada
lista.sort(reverse=True) # ordena de forma decrescente
print(lista)"""

"""nova_lista = sorted(lista) # ordena a lista e a salva em outro lugar 
print(nova_lista)"""

lista = [ # lista de dicionários
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Caroline', 'sobrenome': 'Bento'},
    {'nome': 'João', 'sobrenome': 'Ribeiro'},
    {'nome': 'Pedro', 'sobrenome': 'Fernandes'},
    {'nome': 'Carlos', 'sobrenome': 'Andrade'},
]

def exibir(lista):
    for item in lista:
        print(item)

#######################################################################################################################################################3########

def ordena_por_nome(item):
    return item['nome'] # ele retorna somente os valores correspondentes ao nome, aí ele consegue ordenar o dicionário com base no nome

#######################################################################################################################################################3########

def ordena_por_sobrenome(item):
    return item['sobrenome'] # ele retorna somente os valores correspondentes ao sobrenome, aí ele consegue ordenar o dicionário com base no sobrenome

#######################################################################################################################################################3########


lista.sort(key=ordena_por_nome)

for item in lista:
    print(item)

#######################################################################################################################################################3########

lista.sort(key=ordena_por_sobrenome)

for item in lista:
    print(item)

#######################################################################################################################################################3########


# As duas funções acima são pequenas, tendo apenas uma linha pra sua definição, nesses casos, é melhor utilizar a função lambda
# Sendo assim:

# a palavra 'lambda' vai funcionar como a palavra 'def'
# a primeira palavra 'item' seria o parâmetro da função
# a segunda palavra 'item' seria a passagem do dado que vai ser usado para ordenar
lista.sort(key=lambda item: item['nome'])
exibir(lista)

#######################################################################################################################################################3########

lista.sort(key=lambda item: item['sobrenome'])
exibir(lista)

#######################################################################################################################################################3########

# sorted faz uma cópia rasaf
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
