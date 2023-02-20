# Exercício com classes
# 1 - Crie uma classe Carro (nome)
# 2 - Crie uma classe Motor (nome)
# 3 - Crie uma classe Fabricante (nome)
# 4 - Faça a ligação entre Carro e Motor -> Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante -> Um fabricante pode fazer vários carros 
# Exiba o nome do carro, do motor e do fabricante

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro_1 = Carro('Fusca')
fabricante_1 = Fabricante('Volkswagen')
motor_1 = Motor('1.0')

carro_1.fabricante = fabricante_1
carro_1.motor = motor_1

carro_2 = Carro('Outro carro')
carro_2.fabricante = fabricante_1
carro_2.motor = motor_1
print(carro_1.nome, carro_1.fabricante.nome, carro_1.motor.nome)
print(carro_2.nome, carro_2.fabricante.nome, carro_2.motor.nome)