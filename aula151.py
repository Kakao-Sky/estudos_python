# Funções decoradoras e decoradores com classes

# adiciona_repr -> é uma função decoradora
def adiciona_repr(cls): # funções decoradoras com classes recebem a classe
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

#############################################################################################################
# Por Herança:
# class MyReprMixin():
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
#############################################################################################################
# Por Herança:
# class Time(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome

#     # o repr não vai ficar aqui para evitar a repetição de código
#     # def __repr__(self):
#     #     class_name = self.__class__.__name__
#     #     class_dict = self.__dict__
#     #     class_repr = f'{class_name}({class_dict})'
#     #     return class_repr
    
# class Planeta(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome
#############################################################################################################

# Com decorador:

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    # o repr não vai ficar aqui para evitar a repetição de código
    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr
    
@adiciona_repr    
class Planeta:
    def __init__(self, nome):
        self.nome = nome

br = Time('Brasil')
pt = Time('Portugal')
t = Planeta('Terra')
m = Planeta('Marte')

print(br)
print(pt)

print(t)
print(m)    