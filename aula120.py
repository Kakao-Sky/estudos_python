# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# atributos -> dados dentro da classe
# métodos -> ações e funções dentro da classe
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.

# "Carol" é atributo de "string"
# string = 'Carol' # tipo str -> instância da classe str
# print(string.upper()) # upper é um método que trabalha no dado do objeto string
# print(isinstance(string, str)) # checa se string é uma instância da classe str

class Pessoa: # estou criando a classe "Pessoa"
     # aqui ficam todos os atributos e métodos internos dessa classe

    # (o primeiro parâmetro passado precisa ser "self")
    def __init__(self, nome, sobrenome): # método de inicialização, primeiro a ser executado
        self.nome = nome # p1.nome -> inicializando o atributo, fazendo ele existir
        self.sobrenome = sobrenome # p1.sobrenome 



p1 = Pessoa('Caroline', 'Bento') # aqui estou criando um objeto da classe "Pessoa"
# e passando os parâmetros necessários (nome, sobrenome)
# p1.nome = 'Caroline' # criando um atributo para classe "Pessoa"
# p1.sobrenome = 'Bento'
print(p1)
print(p1.nome)
print(p1.sobrenome)


p2 = Pessoa('Rosana', 'Lopez') 
# p2.nome =  'Rosana'
# p2.sobrenome = 'Lopez'
print(p2)
print(p2.nome)
print(p2.sobrenome)