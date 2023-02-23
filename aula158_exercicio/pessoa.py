from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self):
        self._nome = None
        self._idade = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    @abstractmethod
    def nome(self, nome):...

    
class Cliente(Pessoa):
    def __init__(self):
        super(Cliente, self).__init__()
    
    @Pessoa.nome.setter
    def nome(self, nome):
        self._nome = nome
    

    