# dir, hasattr e getattr em Python
string = 'Luiz'

# 'dir' mostra todos os nomes (atributos, valores, métodos) definidos dentro de um objeto
# 'hasattr' checa se determinado objeto contém determinado nome
#  Exemplo de uso hasattr:
if hasattr(string, 'upper'): # verificando se a string tem o nome 'upper' nela, nesse caso, um método
    # independente do tipo de dado que vai ser verificado, o nome do método é enviado como uma string
    print('Existe upper aqui')
    print(string.upper())

# 'getattr' - pega um nome armazenado em uma variável e utiliza, se for um método existente
string2 = 'Afronagildetina'
metodo = 'upper'
metodo2 = 'lower'

if hasattr(string2, metodo):
    print('Existe ', metodo)
    print(getattr(string, metodo))
    print(string)

if hasattr(string2, metodo2):
    print('Existe ', metodo2)
    print(getattr(string, metodo2))
    print(string)
