'''
Introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar

'''

num_str = input('Digite um número: ')

# respondendo com IF
if num_str.isdigit(): # o problema é que dessa forma ele só reconhece como numero se for int, float é texto
    num_float = float(num_str)
    print(f'O dobro de {num_str} é {num_float * 2}')
else:
    print("Você não digitou um número")

# respondendo com try...except

try:
    print(f'Str: {num_str}')
    num_float = float(num_str)
    print(f'Float: {num_float}')
    print(f'O dobro de {num_str} é {num_float * 2}')
except:
    print("Você não digitou um número")
