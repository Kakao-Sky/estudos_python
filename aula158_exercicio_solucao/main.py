"""

Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem Clientes, Contas e um Banco. A ideia é que o 
Cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas corrente 
têm um limite extra.

Conta(ABC)
    ContaCorrente
    ContaPoupanca

Pessoa(ABC)
    Cliente
        Cliente -> Conta 

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM Conta (Agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra (negativo)
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (superclass) deve ter o método sacar abstrato (Abstração e Polimorfismo - as subclasses que 
    implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e contas (Agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco 
    * Checar se a conta é daquele banco 
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por método
"""