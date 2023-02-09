# raise - lançando exceções (erros)

"""print(123)
raise ValueError('Deu erro') # serve para que você mesmo lance erros nas saídas dos programas, erros que você "escolhe" lançar
print(456)"""

"""def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('Ocorreu um erro, você tentou dividir por 0')
        raise # redundante, ele já ia lançar a exceção, aqui ele tá relançando, a menos que algo seja feito antes de retornar o erro

print(divide(8, 0))"""

def nao_aceito_zero(d):
    if d= 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return True

def deve_ser_numero(x):
    tipo_x = type(x)
    if not isinstance(n, (float, int)):
        raise TypeError(f'"{n}" deve ser int ou float. {tipo_x.__name__} enviado')
    return True

# criando meu próprio erro
def divide(n, d):
    deve_ser_numero(n)
    deve_ser_numero(d)
    nao_aceito_zero(d)


    return n / d

# uma função deve ser definida para a realização de apenas uma tarefa, e seu nome deve ser sugestivo