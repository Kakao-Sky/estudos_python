# Atributos de classe

class Pessoa:
    ano_atual = 2023
    atributo = 'valor' # atributo criado no escopo da classe -> atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Carol', 23)
print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1 # é possível mudar o valor do atributo
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

