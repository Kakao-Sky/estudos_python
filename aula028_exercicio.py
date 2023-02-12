'''
Exercício:
    -Pedir para o user digitar nome
    -Pedir para o user digitar idade
    - Se digitados, exibir:
        Seu nome:
        Seu nome invertido:
        Se o nome tem espaços:
        Qtde de letras:
        Primeira letra:
        Última letra:
    - Nada digitado, exibir:
        Nada digitado
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if(nome and idade):
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if(' ' in nome):
        print('Seu nome tem espaços.')
    else:
        print('Seu nome não tem espaços.')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra é: {nome[0]}')
    print(f'A última letra é: {nome[len(nome) - 1]}')
    # Solução do professor
    print(f'A última letra é: {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios')
