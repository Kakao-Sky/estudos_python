# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗DEVE retornar o novo objeto❗
# __init__ é o método responsável por inicializar a instância. Por isso, init recebe self
# __init__ ❗Ñ DEVE retornar NADA (None❗
# object: é a superclasse de uma classe

# new e init -> são o "construtor" que existe em outras linguagens
# criam e inicializam um objeto, respectivamente

# o new cria o "self" pro init
class A:

    # caso vá passar args pra init, precisa passar aqui tbm
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        return super().__new__(cls) # o super de A é object
        # return object.__new__(A)

    def __init__(self):
        print('Sou o init')

    def __repr__(self):
        return 'A()'

a = A() 
print(a)

# # o que está acontecendo automaticamente:
# a = object.__new__(A) # cria a instância da classe A
# a.__init__() # se existir o init na classe A, chama automaticamente
# print(a)

