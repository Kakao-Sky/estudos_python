# abstractmethod para qualquer método já decorado
# É possível criar @property, @property.setter, @classmethod, @staticmethod e métodos normais como
# abstratos, para isso, use @abstractmethod como decorador interno.
# Foo - Bar são palavras usadas como placeholder para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None # precisa vir antes - configurando property
        self.name = name
    
    @property
    def name(self): 
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name):...

    # @name.setter # não vai precisar do setter, já que a property é abstrata 
    # def name(self, value): 
    #     self._name = value

#############################################################################################################

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name) # passando o parâmetro (name) pra super classe
        # print('sou inútil')

    # usando o setter abstrato
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name





    # name = '' # considerando que a property é um método que se comporta como um atributo, isso já resolveria
    # o problema sem a necessidade de recriar a property     

    # @property # preciso definir a mesma property aqui, já que na super classe ela era abstrata
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     self._name = name

#############################################################################################################

foo = Foo('Bar')
print(foo.name)