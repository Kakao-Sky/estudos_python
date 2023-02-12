# Shallow Copy vs Deep Copy em dados mutáveis Python

# Métodos úteis dos dicionários em Python
#   len - quantidade de chaves**
#   keys - iterável com as chaves
#   values - iterável com os valores
#   items - iterável com chaves e valores
#   setdefault - adiciona valor se a chave não existe
#   copy - retorna uma cópia rasa (shallow copy)
#   get - obtém uma chave
#   pop - apaga um item com a chave especificada (del)
#   popitem - apaga o último item adicionado
#   update - atualiza um dicionário com outro

# tudo é um objeto em python, inclusive dicionário, por isso tem seus métodos

import copy #**

dicio_01 = {
    'chave01': 1,
    'chave02': 2,
}

# a lista também tem o método copy()

dicio_02 = dicio_01 # isso não vai copiar os dados do dicio_01 no dicio_02,
# isso apenas indica que ambos irão apontar pro mesmo lugar na memória, como nas listas

# alterando algo no dicio_02, a modificação afetará dicio_01, porque ambos apontam pro mesmo lugar na memória

""" dicio_02['chave01'] = 4

print(dicio_01, dicio_02) """

# para copiar os valores e cortar as relações, utiliza-se o método copy

dicio_02 = dicio_01.copy()
print(dicio_01, dicio_02)

# ao fazer uma alteração no dicio_02 agora, isso não modificará dicio_01
dicio_02['chave01'] = 4
print(dicio_01, dicio_02) 

# se chama de 'lista rasa' porque ele copiará apenas os valores IMUTÁVEIS
# no caso de ter um valor mutável, como uma lista, ele apenas apontará para o mesmo lugar na memória

d1 = {
    'c1': 1,
    'c2': 2,
    'lista': [0, 1, 2],
}

d2 = d1.copy()
d2['c1'] = 100
print(d1)
print(d2)

d2['lista'][1] = 99999999 # modificará nos dois dicionários
print(d1, 'copy')
print(d2)

# para evitar uma cópia rasa, utiliza-se o método deepcopy, que está 
# dentro do módulo copy, que precisa ser importado**

d1 = {
    'c1': 1,
    'c2': 2,
    'lista': [0, 1, 2],
}

d2 = copy.deepcopy(d1)
d2['c1'] = 100
print(d1)
print(d2)

d2['lista'][1] = 99999999 # modificará nos dois dicionários
print(d1, 'deepcopy')
print(d2)

