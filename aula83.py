# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a

# print(a, b)

"""pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}"""


"""a, b = pessoa # quando o desempacotamento é feito desta forma em dicionários, ele retorna as chaves
print(a, b)

a, b = pessoa.values() # quando o desempacotamento é feito desta forma em dicionários, ele retorna os valores
print(a, b)

a, b = pessoa.items() # quando o desempacotamento é feito desta forma em dicionários, ele retorna uma tupla com chave e valor
print(a, b)

(a1, a2), (b1, b2) = pessoa.items() # fazendo desempacotamento internamente
print(a1, a2)
print(b1, b2)

# fazendo o desempacotamento no for
for chave, valor in pessoa.items():
    print(chave, ': ', valor)"""

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
#######################################################################################################################################################3########

# extraindo os dados de um dicionário e colocando em outro
pessoa_completa = {**pessoa, 'chave': 1, **dados_pessoa} # desempacotamento de um dict dentro de outro
#print(pessoa_completa)

#######################################################################################################################################################3########

# args e kwargs
# args - já foi visto - usa *
# kwargs - keywords arguments (argumentos nomeados) -> sempre usa **

#######################################################################################################################################################3########

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    print()
#######################################################################################################################################################3########

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123,) # função sendo usada para EMPACOTAR
mostro_argumentos_nomeados(**pessoa_completa) # função sendo usada para DESEMPACOTAR

# exemplo de uso, configurações salvas em dict:
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    'arg5': 5,
    'arg6': 6,
}
mostro_argumentos_nomeados(**configuracoes)