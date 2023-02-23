# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar módulos como 
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass


# @dataclass
# class Pessoa:
#     nome: str
#     idade: int


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz', 30)
#     p2 = Pessoa('Luiz', 30)
#     print(p1 == p2)

# parte 2
# @dataclass
# class Pessoa:
#     nome: str
#     # idade: int
#     sobrenome: str

#     @property
#     def nome_completo(self):
#         return f'{self.nome} {self.sobrenome}'

#     @nome_completo.setter
#     def nome_completo(self, valor):
#         nome, *sobrenome = valor.split()
#         self.nome = nome
#         self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     # p1 = Pessoa('Luiz', 30)
#     # p2 = Pessoa('Luiz', 30)
#     # print(p1 == p2)
#     p1 = Pessoa('Luiz', 'Otávio')
#     p1.nome_completo = 'Maria Helena'
#     print(p1)
#     print(p1.nome_completo)

# parte 3

# @dataclass
# @dataclass(init=False)
# class Pessoa:
#     nome: str
#     sobrenome: str

#     @property
#     def nome_completo(self):
#         return f'{self.nome} {self.sobrenome}'

#     @nome_completo.setter
#     def nome_completo(self, valor):
#         nome, *sobrenome = valor.split()
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = ' '.join(sobrenome)
#         self.sobrenome = sobrenome
#         self.nome_completo = f'{self.nome} {self.sobrenome}'

#     def __post_init__(self):
#         print('POST INIT')

#     # @property
#     # def nome_completo(self):
#     #     return f'{self.nome} {self.sobrenome}'

#     # @nome_completo.setter
#     # def nome_completo(self, valor):
#     #     nome, *sobrenome = valor.split()
#     #     self.nome = nome
#     #     self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz', 'Otávio')
#     p1.nome_completo = 'Maria Helena'
#     print(p1)
#     print(p1.nome_completo)

# Parte 4
# @dataclass(init=False)
# @dataclass(repr=True)
# class Pessoa:
#     nome: str
#     sobrenome: str

#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.nome_completo = f'{self.nome} {self.sobrenome}'

#     def __post_init__(self):
#         print('POST INIT')

#     # @property
#     # def nome_completo(self):
#     #     return f'{self.nome} {self.sobrenome}'

#     # @nome_completo.setter
#     # def nome_completo(self, valor):
#     #     nome, *sobrenome = valor.split()
#     #     self.nome = nome
#     #     self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz', 'Otávio')
#     print(p1)
#     print(p1.nome_completo)
#     lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
#     ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
#     print(ordenadas)

# parte 5
# from dataclasses import dataclass
# from dataclasses import asdict, astuple, dataclass


# @dataclass(repr=True)
# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str


# if __name__ == '__main__':
#     lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
#     ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
#     print(ordenadas)
#     p1 = Pessoa('Luiz', 'Otávio')
#     print(asdict(p1).keys())
#     print(asdict(p1).values())
#     print(asdict(p1).items())
#     print(astuple(p1)[0])

# Parte 6
from dataclasses import asdict, astuple, dataclass
from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str = 'missing'
    sobrenome: str = 'not sent'
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)