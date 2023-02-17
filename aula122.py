# entendendo Self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da classe (objeto) - Tem os dados
# uma classe pode gerar várias instâncias
# Na classe, o self é a própria instância

class Carro:
    def __init__(self, nome='Sem nome'):
        # self.nome = 'Fusca' # Hard coded
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} acerelou')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
Carro.acelerar(celta)
