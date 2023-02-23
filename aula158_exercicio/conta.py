from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def info(self, msg=''):
        print(f'Seu saldo é {self.saldo:.2f} ({msg})')

    @abstractmethod
    def sacar(self, valor):...

##############################################################################################################

class ContaCorrente(Conta):
    def __init__(self, agencia, num_conta, saldo, limite):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor 
            self.info(f'SAQUE EFETUADO: {valor}')
        else: 
            self.info('SAQUE NEGADO')

##############################################################################################################

class ContaPoupanca(Conta):
    def __init__(self, agencia, num_conta, saldo=0):
        super().__init__(agencia, num_conta, saldo)

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor 
            self.info(f'SAQUE EFETUADO: {valor}')
        else: 
            self.info('SAQUE NEGADO')
        
##############################################################################################################

if __name__ == '__main__':
    cp1 = ContaPoupanca(1, 2, 0)
    cp1.sacar(1)
    cp1.depositar(452.5)
    cp1.sacar(74.89)
    print('#######################')
    cp2 = ContaPoupanca(1302, 225485)
    cp2.sacar(1)
    cp2.depositar(800)
    cp2.sacar(74.89)
    print('#######################')
    cc1 = ContaCorrente(1302, 225485, 0, 100)
    cc1.sacar(1)
    cc1.depositar(800)
    cc1.sacar(74.89)
    print('#######################')