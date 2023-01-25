# EXERCÍCIO
# Exiba os índices da lista

lista = ['Maria', 'Helena', 'Carroline']

# MINHA solução
i = 0
for nome in lista:
    print(i, lista[i])
    i += 1 

# solução do PROFESSOR
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])