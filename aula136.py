# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também 
# são apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # criando a instância de Endereco dentro de Cliente
        # qnd o cliente n existir mais, a instância de endereço é apagado também
    
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self): # destructor
        print('APAGANDO: ', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    def __del__(self):
        print('APAGANDO: ', self.rua, self.numero)

cliente1 = Cliente('Mary')
cliente1.inserir_endereco('Av Brasil', 25)
cliente1.inserir_endereco('Rua AB', 6545)
endereco_externo = Endereco('Av Saudade', 12354)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1 # apagando o objeto pai

print('########## AQUI TERMINA MEU CÓDIGO ##########')