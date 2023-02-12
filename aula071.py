# args - Argumentos não nomeados
# * - *args (empacotamento e desempacotamento)

# Desempacotamento

x, y, *resto = 1, 2, 3, 4

print(x, y, resto)

""" def soma(x, y):
    return x + y """

""" def soma(*args):
    total = 0 # acumulador
    for numero in args:
       # print('Total: ', total, numero)
        total += numero
       # print('Total: ', total)
        return total -> o erro estava AQUI, PQ RETURN FICA ALINHADO COM FOR

    print(args, type(args))

soma_1_2_3 = soma(1, 2, 3, 4, 5)
print(soma_1_2_3) """


# Parte 2 - *args
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)   

outra_soma = soma(1, 4, 5, 78, 9, 63, 52, 12)
print(outra_soma)

# no Python já existe uma função pra soma, chamada sum()
print(sum((1, 4, 5, 78, 9, 63, 52, 12))) # essa função recebe um iterável (no caso, uma tupla)

# no caso da função sum(), ela necessita que seja passado um iterável, então, a seguinte situação seria 
# totalmente possível:
numeros = 1, 4, 5, 78, 9, 63, 52, 12, 3, 4, 68
print(sum(numeros))

# mas no caso da nossa função soma(), isso geraria um erro, pq *args faz o empacotamento dos argumentos 
# que estamos enviando, transformando-os em uma tupla, portanto, nesse caso seria necessário 
# fazer o desempacotamento:

print(soma(*numeros))
