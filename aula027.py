'''

Fatiamento de Strings
012345678
Olá mundo
987654321 (negativo)
Fatiamento [i:f:p] [::]
    i - início do fatiamento
    f - fim do fatiamento
    p - passo (de qnt em qnt ele vai pular)

Obs.: a função len retorna a quantidade de caracteres da str

'''

#strings são iteráveis - aula 24
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])

print(variavel[4:]) #pega do índice 4 até o fim da str
print(variavel[4:7]) # o índice 7 é d, mas ele não pega o último índice da contagem
print(variavel[4:8]) # tem que colocar um número a mais

# em pyhon, o último índice não é incluso

print(variavel[0:5]) # vai do início ao quarto índice
print(variavel[:5]) # vai do início ao quarto índice

print(variavel[-8:-2]) # é possível usar os índices negativos

print(len(variavel))
print(len(variavel[3]))

print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[0:len(variavel):3])
print(variavel[::-1])
print(variavel[-1:-10:-1])
