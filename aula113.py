# reduce - fz a redução de um iterável em um único valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# total = 0
# for p in produtos:
#     total +=p['preco'] # acumulador

# print(total)

###########################################################################################################################################################

# a função reduce() precisa de um acumulador

def funcao_do_reduce(acumulador, produto):
    print(acumulador)
    print(f'{produto=}')
    return acumulador + produto['preco']

#               função          iterável   valor inicial
total = reduce(funcao_do_reduce, produtos, 0) 
print(f'{total=}')

# usando lambda
total2 = reduce(
    lambda ac, p: ac + p['preco'], # func do reduce - lambda - retorne acumulador, produto, some o preço do produto no acumulador
    produtos, # iterável
    0 # valor inicial, sempre bom colocar
)