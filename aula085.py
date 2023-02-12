# List comprehension com mais de um For 

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

# com list comprehension

lista = [
    (x, y) 
    for x in range(3)
    for y in range(3) # esse for está dentro do for acima
]
print(lista)

# list comprehension dentro de list comprehension
lista = [
    [letra for letra in 'Carol'] # as letras do nome serão colocadas em listas dentro da lista
    for x in range(3) # durante a execução desse for
]
print(lista)
