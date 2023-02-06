# List comprehension em Python
# É uma forma rápida de criar listas a partir de iteráveis

#print(list(range(10)))

import pprint # pretty print

# criando uma função pra pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

###############################################################################################################################################################


lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

# Fazendo a mesma coisa com list comprehension
lista = [numero for numero in range(10)]
print(lista)

#######################################################################################################################################################3########
lista = [ # exemplo de mapeamento de dados
    numero * 2
    for numero in range(10) 
    ]
print(lista)

#######################################################################################################################################################3########
#######################################################################################################################################################3########

# Mapeamento de dados em list comprehension
# é quando você pega um iterável, que tem x dados, e cada dado é modificado e colocado em uma lista (ou outro iterável),
# o que vai fazer com que ambos os iteráveis tenham o mesmo tamanho 

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [produto for produto in produtos]
#print(novos_produtos)
# fazendo o desempacotamento dos dados e separando-os por uma quebra de linha
print(*novos_produtos, sep='\n')

novos_produtos = [produto['nome'] for produto in produtos]
print(novos_produtos)
# fazendo o desempacotamento dos dados e separando-os por uma quebra de linha
print(*novos_produtos, sep='\n')

novos_produtos = [produto['preco'] for produto in produtos]
print(novos_produtos)
# fazendo o desempacotamento dos dados e separando-os por uma quebra de linha
print(*novos_produtos, sep='\n')

print(novos_produtos)
# fazendo o desempacotamento dos dados e separando-os por uma quebra de linha
print(*novos_produtos, sep='\n')


# como neste caso estamos lidando com um dicionário, não há necessidade de escrever todas as suas chaves,
# pode-se apenas desempacotar o mesmo:
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # estou criando um novo dicionário dentro da lista, que repete os produtos, mas aumenta seu preço
    for produto in produtos
] 
print(*novos_produtos, sep='\n')


# estou criando um novo dicionário dentro da lista, que repete os produtos, mas aumenta seu preço apenas se o preço original
# for maior que 20 
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} # if ternário
    for produto in produtos
] 
print(*novos_produtos, sep='\n')



###############################################################################################################################################################
###############################################################################################################################################################
# Filtro de dados em List comprehension(filter)



