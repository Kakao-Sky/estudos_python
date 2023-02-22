""" Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""

var_1 = 1

class Foo:
    def soma(self, x: int or float, y: int or float) -> int or float:
        """
        Soma x e y

        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y
        

    def multiplica(self,
        x: int or float,
        y: int or float,
        z: int or float or None
    ) -> int or float:
        """Multiplica x, y e/ou z
        
        Multiplica x e y. /se z for enviado, multiplica x, y, z"""
        if z is None:
            return x * y 
        return x * y * z
    
    def bar(self) -> int:
        """O que o método faz
        
        :raises NotImplementedError: Se o método não for definido"""
        raise NotImplementedError('Teste')

var_2 = 2
var_3 = 3
var_4 = 4

