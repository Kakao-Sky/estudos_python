# Tipo tupla - lista imutável
# é imutável como uma string
# é mais eficiente que uma lista

# Formas de criar:
# Sem (), nem []
nomes = 'Ana', 'Bárbara', 'Caroline'
print(type(nomes))
print(nomes)

# Com () no lugar dos [] da lista
nomes2 = ('Carol', 'Luiza', 'Jenifer')
print(type(nomes2))
print(nomes)

# Com coerção de tipos:
lista_nomes = ['Carol', 'Joana', 'Lucas']
tupla_nomes = tuple(lista_nomes)

print(type(lista_nomes), type(tupla_nomes))
print(tupla_nomes)

print(nomes[2])
print(nomes[-3])