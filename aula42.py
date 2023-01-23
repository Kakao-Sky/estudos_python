# iteração de strings com while 
# qual letra apareceu mais vezes

frase = 'O Python é uma linguagem de programação' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'

i = 0
quantidade = 0
contador = 0
letra_repetida = ''
while i < len(frase):
    letra_atual = frase[i]
    quantidade = frase.count(letra_atual)
    
    # solução dada pelo professor para não incluir espaços
    if letra_atual == ' ':
        i += 1
        continue

    if(contador < quantidade):
        contador = quantidade
        letra_repetida = letra_atual

    i += 1

print(f'A letra "{letra_repetida}" foi a mais repetida, tendo {contador} repetições')

# solução muito próxima à do professor  