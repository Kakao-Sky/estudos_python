# Listas dentro de listas
# Listas de listas e seus índices

salas = [
    #   0         1     -> itens dentro da lista interna
    ['Maria', 'Helena', ], # item 0 -> primeira lista
    #   0               -> itens dentro da lista interna
    ['Elaine', ], # item 1 -> segunda lista
    #   0       1       2       -> itens dentro da lista interna
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # item 2 -> terceira lista
]

print(salas)
print(salas[1])
print(salas[0][1]) # buscando 'Helena'
print(salas[2][2]) # buscando 'Eduarda'
print(salas[2][3][2]) # buscando 20

for sala in salas:
    print(sala) # pega as listas internas

for sala in salas:
    print(f'A sala é: {sala}')
    for item in sala:
        print(item) # pega os valores dentro das listas internas
