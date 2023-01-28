# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

""" a, b, c, *_ = lista
print(a, c)

p, b, *_, ap, u = lista # p - primeiro; u - último; ap - antepenúltimo
print(p, u, ap)
 """

for nome in lista:
    print(nome, end=' ') # Deixa tudo em uma só linha

# forma de pegar os itens da lista sem precisar do for (fazer desempacotamento):
print('Maria', 'Helena', 1, 2, 3, 'Eduarda') # só pra mostrar que é igual
print(*lista)
print(*string)
print(*tupla)

salas = [
    #   0         1     -> itens dentro da lista interna
    ['Maria', 'Helena', ], # item 0 -> primeira lista
    #   0               -> itens dentro da lista interna
    ['Elaine', ], # item 1 -> segunda lista
    #   0       1       2       -> itens dentro da lista interna
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # item 2 -> terceira lista
]

print(*salas)
print(*salas, sep='\n') # o separador dos itens é a quebra de linha