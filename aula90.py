# Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)
# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

# iterável - um item sequencial (detém os valores)
# iterator - entrega um valor por vez do iterável 

print(next(iterator))
print(next(iterator))
print(next(iterator))

# se eu chamar o próximo elemento depois de a minha sequência já ter acabado, ele vai levantar uma exceção
# o for trata isso automaticamente 

#############################################################################################################################################################
#############################################################################################################################################################

# Generator expression, Iterables e Iterators em Python

iterable = ['eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
lista = [n for n in range(100000)] # list comprehension
generator = (n for n in range(100000)) # generator expression
print(sys.getsizeof(lista)) # pegando o tamanho da lista, pra comparar com o tamanho do generator
print(sys.getsizeof(generator)) 

# o generator acaba sendo mais leve na memória que a lista porque ele só entrega um valor por vez, já a lista já armazena todos os valores na memória
# generator não tem tamanho, nem índice, mas a lista tem