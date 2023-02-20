# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, ao invés de recebermos 
# a instância no primeiro parâmetro, recebemos a própria classe.

class Pessoa:
    ano = 2023 # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # decorator que indica que é um método de classe
    def metodo_de_classe(cls): # precisa passar o parâmetro cls, que significa a própria classe
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

print(Pessoa.ano)    
Pessoa.metodo_de_classe()
p1 = Pessoa('João', 32)
p2 = Pessoa.criar_com_50_anos('Julia')
print(p2.nome, p2.idade)

