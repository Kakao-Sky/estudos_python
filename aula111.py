# map - para mapear dados

from functools import partial

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 107.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#############################################################################################################
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

# retorna uma closure
aumenta_dez_porcento = partial(
    aumentar_porcentagem, 
    porcentagem=1.1
)

def muda_preco_produtos(produto):
    return {**produto,
     'preco':aumenta_dez_porcento(produto['preco'])}
    

# fazendo mapeamento pelo map
# recebe a ação a ser realizada no mapeamento(poderia ser uma lambda) e o iterável a ser mapeado
novos_produtos = map(muda_preco_produtos, produtos)

print_iter(produtos)
print_iter(novos_produtos)








# # fazendo mapeamento por list comprehension
# novos_produtos = [
#     {**produto, 'preco':aumenta_dez_porcento(produto['preco'])}
#     for produto in produtos
# ]


# {**produto, 'preco':aumentar_porcentagem(produto['preco'], 1.1)}
# desempacote cada produto de produtos, pegue o preço e altere pelo valor que tem lá aumentando 10% 
# for produto in produtos
# para cada produto em produtos
#############################################################################################################

    


