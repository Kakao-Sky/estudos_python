# Retorno de valores das funções (return)

variavel = print('Carol')
print(variavel) # a função print() retorna um valor None

def soma(x, y):
    print(x + y)

variavel = soma(4, 5) # a função soma() será executada, mas retorna o valor None
print(variavel)

def soma2(x, y):
    if x > 10:
        return 10, 20
    return (x + y) # return faz a função retornar algum valor
    # depois do return, nada mais executa dentro da função, ele indica onde ela termina

soma1 = soma2(2, 3)
soma_ = soma2(5, 8)
# print(soma1 + soma_)
print(soma2(11, 5))
print(soma2(1, 5))

# print() != return
# o print() é uma função, que mostra algo na tela, mas não retorna nada
# o return é usado para retornar


