'''
Formatação básica de strings

s - string
d - int
f - float 
.<número de dígitos>f
x ou X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
ex.: 0>-100,.1f
Conversion flags - !r !s !a

'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preenche todos os espaços à esquerda com ' ' até que a qtde chegue a 10
print(f'{variavel: <10}')# preenche todos os espaços à direita com ' ' até que a qtde chegue a 10
print(f'{variavel:-<10}')# preenche todos os espaços à direita com '-' até que a qtde chegue a 10
print(f'{variavel: ^10}')# preenche todos os espaços à direita e à esquerda com ' ' até que a qtde chegue a 10
print(f'{variavel:-^10}')# preenche todos os espaços à direita e à esquerda com '-' até que a qtde chegue a 10
print(f'{1000.4566624168952:+,.3f}')
print(f'O hexadecimal de 15654 é {15654:08X}')
