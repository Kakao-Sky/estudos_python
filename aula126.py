# __dict__ e vars para atributos de instância
# __dict__: está dentro das instâncias da classe e mantém um dicionário 
#  dos atributos da instância que podem ser escritos.
# vars -> mostra o __dict__ de uma instância
class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
# p1.nome = 'AAAAAAAAAA'
# p1.nome está dentro do __dict__
# del p1.nome
print(p1.__dict__)
print(vars(p1))