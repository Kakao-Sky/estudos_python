# filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def filtrar_preco(produto):
    return produto['preco'] > 10


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print_iter(produtos)

# # filtrando com list comprehension:
# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10 # filtro
# ]

# map -> altera os valores, mas mantém o mesmo tamanho do iterável anterior
# filter -> pode ter um iterável de tamanho diferente do anterior

# usando o filter()
novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)
print_iter(novos_produtos)

# mesma coisa usando uma função que não é lambda
novos_produtos = filter(
    filtrar_preco,
    produtos
)
print_iter(novos_produtos)
