"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar
apenas uma letra
- Quando o usuário digitar uma letra, você irá verificar se a letra está na palavra secreta.
    - Se a letra digitada estiver na na palavra secreta; exiba a letra;
    - Se a letra não estiver, exiba *.
Faça a contagem de tentativas do seu usuário

"""

# MINHA tentativa de solução
""" palavra_secreta = 'abelha'
palavra_formatada = '******'
letra = ''
j = 0
while '*' in palavra_formatada:
    letra = input('Digite uma letra: ')

    if(len(letra) > 1):
        print('Digite apenas uma letra.')
    else:
        for i in palavra_secreta:
            if letra in palavra_secreta[j]:
                print(palavra_secreta[j])
                palavra_formatada[j] = letra
                j += 1 """

# solução do PROFESSOR

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if  letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta:
        if (letra in letras_acertadas):
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você acertou')
        print('A palavra era ', palavra_secreta)
        print('Tentativas necessárias: ', tentativas)
        letras_acertadas = ''
        tentativas = 0