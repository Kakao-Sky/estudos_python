# Funções Lambda complexas

def executa(funcao, *args):
    return funcao(*args)


"""def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica"""

# próximas 3 linhas: função cria_multiplicador em lambda
duplica = executa(lambda m: lambda n: n*m, 2)
triplica = executa(lambda m: lambda n: n*m, 3)
quadruplica = executa(lambda m: lambda n: n*m, 4)


print(duplica(2))
print(triplica(2))
print(quadruplica(2))

print(
    executa(lambda x, y: x + y, 2, 3), # essas duas linhas fazem praticamente a mesma coisa, mas a de cima é uma função lambda
    #executa(soma, 2, 3)
) 
