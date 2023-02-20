# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str): # herda tudo da classe str
#     def upper(self): # sobrescreveu o método upper() da classe str
#         # return 'ABCD'
#         print('CHAMOU O UPPER DA SUBCLASSE')
#         return super().upper() # chamando o método upper() da classe str, o real
#         # super() -> recebe uma classe e o primeiro argumento
#         # neste caso -> super(MinhaString, self) 


# string = MinhaString('carol')
# print(string) 
# print(string.upper())


class A:
    def __init__(self, atributo):
        self.atributo = atributo

    atributo_a = 'valor A'
    def metodo(self):
        print('A')


class B(A):
    def __init__(self, atributo, outra_coisa): # esse init sobrescreve o init de A, mas precisa repassar 
        super().__init__(atributo) # o atributo para o A mesmo assim, porém, pode ter outros atributos únicos
        self.outra_coisa = outra_coisa

    atributo_b = 'valor B'
    def metodo(self):
        print('B')
        

class C(B):
    def __init__(self, *args, **kwargs):
        super(C, self).__init__(*args, **kwargs)
        print('Inicializando... os args repassados não me importam, apenas repasso pra cima')


    atributo_c = 'valor C'
    def metodo(self):
        # super(C, self).metodo() # "eu sou o C, a partir de mim, procure o método acima"
        # super(B, self).metodo() # "eu sou o B, a partir de mim, procure o método acima"
        A.metodo(self) # -> super(B, self).metodo() -> mesma coisa
        print('C')
        
# c = C()
c = C('atributo pedido em A', 'atributo pedido em B') # como a classe A agora pede um atributo de
# inicialização, ele tem que ser repassado, bem como o atributo pedido em B
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo() # quando chamado, executa o metodo de B, puq chamei ele com o super()
# print(C.mro()) # mostra a MRO da Classe C