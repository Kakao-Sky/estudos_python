# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# o "return" para a execução de uma função, com generator, as funções podem simplesmente pausar
# no lugar do "return", as generator functions utilizam "yield"

def generator(n=0):
    yield 1 # funciona como o "return", mas não para a execução - pausa aqui
    print('Continuando...') # pode ter código entre as pausas
    yield 2 # pausou de novo
    print('one more time')
    yield 3 # mais uma pausa
    print('Vou terminar')
    return 'ACABOU' # fim da execução
    # esse return vai ser executado quando depois que os valores do generator acabarem, o que vai gerar uma exeção, aí chega no return, e para a execução

"""gen = generator(n=0)
print(gen)
print(next(gen)) # executa o primeiro yield e pausa a execução da função
print(next(gen)) # continua a execução do ponto em que parou, até chegar ao término da execução da função, ou até chegar à próxima pausa
print(next(gen)) # mais uma vez, continua de onde parou 
print(next(gen)) # fim da execução"""

# refazendo a execução de forma dinâmica:
gen = generator(n=0)
for n in gen:
    print(n)

###############################################################################################################################################################
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator()
for n in gen:
    print(n)