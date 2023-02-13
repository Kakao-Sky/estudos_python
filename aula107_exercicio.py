# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# MINHA SOLUÇÃO

from itertools import zip_longest #**


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

tam_cidades = len(cidades)
tam_estados = len(estados)

print(cidades)
print(estados)
item_apagado = -1

if(tam_cidades > tam_estados):
    item_apagado = tam_cidades - 1
    del cidades[item_apagado]
elif(tam_cidades < tam_estados):
    item_apagado = tam_estados - 1
    del estados[item_apagado]
else:
    item_apagado = None

print(cidades)
print(estados)

lista_zipper = []

for i in range(tam_cidades):
    lista_zipper.append(f'({cidades[i]}, {estados[i]})')

print(lista_zipper)

############################################################################################################################################################

# solução do PROFESSOR

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    # print(min(1, 2)) # retorna o menor entre dois valores ou iteráveis
    # print(max(1, 2)) # retorna o maior entre dois valores ou iteráveis
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))

# Python já tem pronto
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE'))) #**