# enumerate - enumera iteráveis (índices)

# exercício da aula 50

lista = ['Maria', 'Helena', 'Carroline']
lista.append('João')

lista_enumerada = enumerate(lista)

print(lista_enumerada) # vai mostrar um objeto estranho, puq é um iterator (Aula 74)
print(next(lista_enumerada))

for item in lista_enumerada: # pode gerar um problema em algum momento, pq o iterator tá dentro de uma var
    print(item)

# pode-se fazer da seguinte forma:
for item in enumerate(lista): 
    print(item)

# pode-se também usar a variável, caso queira, tornando o iterator uma lista
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)


# utilizando o desempacotamento:
for item in enumerate(lista): # gera tuplas como resultado, que serão colocadas dentro da lista
    indice, nome = item
    print(indice, nome) 
