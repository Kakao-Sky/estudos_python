# TEORIA: Herança, generalização e especialização
# Herança simples - Relações entre classes
# Associação - usa 
# Agregação - tem (e usa)
# Composição - é dono de (e tem)
# Herança - é um 
# 
# Herança ou Composição
# 
# Classe principal (Pessoa)
#   -> super class, base class, parent class, class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class Foo(object): # o python faz automaticamente a herança do built-in "object" quando se cria uma classe
#     ...

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Função executada na classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Função executada na classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    ...

c1 = Cliente('Kamili', 'Piccoli')
c1.falar_nome_classe()
a1 = Aluno('Aline', 'Sousa')
a1.falar_nome_classe()


