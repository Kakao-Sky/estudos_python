# Classes decoradoras (Decorator classes)

class Somar:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self.func(*args, **kwargs)


@Somar
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
##############################################################################################################
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(2)
def multi(x, y):
    return x * y


dois_vezes_quatro = multi(2, 4)
print(dois_vezes_quatro)