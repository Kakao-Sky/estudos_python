# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos 

from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


pessoas = ['João', 'Joana', 'Luiz', 'Letícia']

camisetas = [
    ['preta', 'branca'], 
    ['P', 'M', 'G'],
    ['masculino', 'feminino'],
    ['algodão', 'canelada']
    ]

print(combinations(pessoas, 2)) # para ver as combinações de "pessoas" em grupos de dois
# print(*list(combinations(pessoas, 2)), sep='\n')
print_iter(combinations(pessoas, 2))
print_iter(combinations(pessoas, 3))
print_iter(permutations(pessoas, 2))
print_iter(permutations(pessoas, 3))
print_iter(permutations(pessoas, 4))

print_iter(product(*camisetas)) # produto cartesiano - aumenta exponencialmente 
