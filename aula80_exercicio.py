"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    # [0] - nenhum duplicado (-1)
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],     # [1] - 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],     # [2] - 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],     # [3] - 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],    # [4] - 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],     # [5] - 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  # [6] - 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],     # [7] - 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],    # [8] - 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],     # [9] - 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],     # [10]- 1
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],    # [11]- nenhum duplicado (-1)
]

# MINHA solução - não funciona
""" numeros = set()
duplicado = None
for lista in lista_de_listas_de_inteiros:
    for numero in lista:
        if numero not in numeros:
            numeros.add(numero)
        else:
            duplicado = numero
            numeros.clear()
            continue
    if duplicado is not None:
        print('Duplicado: ', duplicado)
    else:
        print(-1)
    duplicado = None """
    
# solução do PROFESSOR

def encontra_primeiro_duplicado(lista_de_inteiros):

    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)      

    return primeiro_duplicado



for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_primeiro_duplicado(lista))

# mesma lógica que eu tinha pensado, mas por ele usar função, consegue analisar lista por lista sem ter um valor anterior atrapalhando 
