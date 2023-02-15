# Funções recursivas e recursividade
# - funções que podem se chamar de volta (elas chamam elas mesmas)
# - úteis p/ dividir problemas grandes em problemas menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores;
# - Um caso recursivo que resolve o pequeno problema;
# - Um caso base para a recursão.
# - Ex.: fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

# import sys 

# sys.setrecursionlimit(1004) # aumentando o limite de recursão

# def recursiva(inicio=0, fim=10):

#     print(inicio, fim) # aqui dá pra ver o 10 - 10

#     # Caso base (o que vai fazer a chamada em loop parar):
#     if inicio >= fim:
#         return fim
    
#     # print(inicio, fim)

#     # caso recursivo -> contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())


# Função fatorial:
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(4))