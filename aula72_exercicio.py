# Exercício com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor da variável.

# MINHA SOLUÇÃO
def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

multiplicacao = multiplicar(1, 4, 5, 8, 9, 6)
print(f'{multiplicacao=}')


# Crie uma função que fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar

# MINHA SOLUÇÃO
def impar_par(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

print(impar_par(5))
print(impar_par(8))
