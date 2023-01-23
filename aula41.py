# while / else

nome = input('Digite seu nome: ')

i = 0
while i < len(nome):
    letra = nome[i]

    if letra == ' ':
        print('Seu nome tem espaços')
        break
    print(letra)
    i += 1
else:
    print('Seu nome não tem espaços')
