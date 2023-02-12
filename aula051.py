# Empacotamento e desempacotamento:
# Introdução ao desempacotamento 

nomes = ['Maria', 'Helena', 'Carroline']

# para extrair os valores da lista e colocar em variáveis:
nome1, nome2, nome3 = nomes # qtde de var receptoras == qtde de itens na lista
print(nome2)

# outra forma de fazer o código acima seria:
nome1, nome2, nome3 = ['Maria', 'Helena', 'Carroline']
print(nome3)

# ERRO -> too many values to unpack:
# nomes = ['Maria', 'Helena', 'Carroline']
# nome1, nome2, nome3 = nomes

# ERRO -> not enough values to unpack:
# nomes = ['Maria', 'Helena', 'Carroline']
# nome1, nome2, nome3, nome4 = nomes

# os códigos vistos acima fazem o DESEMPACOTAMENTO da lista, e atribuem os valores às variáveis separadas
# se quiser pegar até uma posição X, pode-se criar uma variável de RESTO
# para utilizar a variável de resto, é necessário fazer o EMPACOTAMENTO dos outros valores

nome1, *restante = nomes
print(nome1)
print(restante)

# por convensão, não se usa 'restante', já que a variável não será utilizada no código novamente
# se utiliza '_'

nome1, *__ = nomes
print(nome1)
print(__)

# para pegar um valor cuja posição NÃO é a primeira
__, nome2, *__ = nomes
print(nome2, __)
