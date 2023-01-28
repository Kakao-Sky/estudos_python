# Imprecisão do ponto flutuante 
# Double-precision float-point format IEEE 754
# https://en.wikipedia.org/wiki/Double-precision_floating-point_format
# https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

import decimal #*


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # tem como valor um número impreciso

# formas de tornar o número mais preciso:

# pela formatação:
print(f'{numero_3:.2f}')

# pela função de arredondamento:
print(round(numero_3, 2)) # essa função irá arredondar o resultado para duas casas decimais
# variável a ser arredondada, número de casas decimais, mas ele não mostra a última casa decimal se for 0

# pelo módulo (decimal) do python: *
# utilizado apenas em números com muitas casas decimais, que precisam de uma precisão extrema (científico)
numero_1 = decimal.Decimal('0.2')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
