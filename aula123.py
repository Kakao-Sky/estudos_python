# Escopo da classe e métodos da classe

class Animal:
    # nome = 'leão'
    def __init__(self, nome): # agora só vai poder ser acessado pelas instâncias da classe
        self.nome = nome

        variavel = 'valor qualquer' # variável interna do escopo do __init__
        print(variavel)
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

# print(nome) # não pode acessar a variável 'nome' daqui, pq ela é de dentro do escopo da classe 
# print(Animal.nome) # uma das formas de acessar 

leao = Animal(nome='Leão') 
print(leao.nome) # vai chamar tudo do __init__
# print(leao.acao())
print(leao.comendo('queijo'))
