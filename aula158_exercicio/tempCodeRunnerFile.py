from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def _conta(self):...

    @abstractmethod
    def sacar(self, agencia, numero_da_conta, saldo, valor_a_sacar, autenticacao):...

    def depositar_conta(self, agencia, numero_da_conta, valor):...

##############################################################################################################

class ContaCorrente(Conta):
    def _conta(self):
        self._conta_ = {}

    
    @property
    def conta(self):
        return self.conta
    @conta.setter
    def conta(self, nome_cliente, agencia, numero_da_conta, saldo, tipo_conta):
        self._conta_ = {
            'Cliente': nome_cliente,
            'Agência': agencia,
            'Numero da conta': numero_da_conta,
            'Saldo': saldo,
            'Tipo de conta': tipo_conta
        }

    def sacar(self, agencia, numero_da_conta, saldo, valor_a_sacar, autenticacao):
        self._agencia = agencia
        self._numero_da_conta = numero_da_conta
        self._saldo = saldo
        self.valor_a_sacar = valor_a_sacar
        self._autenticacao = autenticacao
        
        if self._autenticacao:
            ...