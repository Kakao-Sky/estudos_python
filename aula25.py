'''

Interpolação básica de strings (mesma coisa feita com o 'format')
Formata strings parecido com o método format (aula 14)

s - string 
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Carol'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

# é possível fazer a interpolação com valores que não estejam em variáveis
print('O hexadecimal de %d é %04X' % (12, 12)) #04x - 04 indica que ele deve preencher as casas decimais com 0
