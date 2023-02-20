# Encapsulamento (modificadores de acesso: public, _protected, __private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções:
#   (sem underline) = public
#       pode ser usado em qualquer lugar
#   _ (um underline) = protected
#       NÃO DEVE ser usado fora da classe ou suas subclasses
#   __(dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python -> _NomeClasse__nome_attr_ou_method (fica assim)
#        SÓ DEVE ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso aqui é público'
        self._protected = 'isso aqui é protegido'
        self.__private = 'isso aqui é privado'

    def metodo_publico(self):
        # totalmente possível acessar os métodos (e atributos) protegidos em outros métodos 
        #  dentro da classe
        print(self._metodo_protegido())
        return 'metodo_publico'

    def _metodo_protegido(self):
        print(self.__metodo_private())
        return '_metodo_protegido'

    def __metodo_private(self): # só pode ser acessado dentro da classe, em qualquer parte dela
        print(self.__private)
        return '__metodo_private'

f = Foo()
print(f.public)
print(f.metodo_publico())
# print(f._protected)
# print(f._metodo_protegido()) # má prática

