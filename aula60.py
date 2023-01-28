# Operação ternária (condicional de uma linha) - operadores ternários
# <valor> if <condição> else <outro valor>

print('Valor' if True else 'Outro valor')

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

# Validando dígito CPF
digito = 11 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
print(novo_digito)