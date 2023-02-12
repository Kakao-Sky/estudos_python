"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se o mesmo é par ou ímpar. Caso
o usuário não digite um número inteiro, informe que o número não é inteiro.

"""
num_str = input("Digite um número inteiro: ")

if num_str.isdigit():
    num_int = int(num_str)
    if num_int % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar")
else:
    print("Você não digitou um número inteiro")

""" 
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação 
apropriada. Ex.: Bom dia 0-11; Boa tarde 12-17 e Boa noite 18-23

"""
hora_str = input("Que horas são? ")

if hora_str.isdigit():
    hora_int = int(hora_str)
    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia")
    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde")
    elif hora_int >= 18 and hora_int <= 24:
        print("Boa noite")
    else:
        print("Esse horário não existe")
else:
    print("Você não digitou um horário")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 5 letras ou menos, escreva 
"Seu nome é curto"; se tiver entre 5 e 6, escreva "seu nome é normal"; maior que 6, escreva "Seu nome é 
muito grande"

"""

primeiro_nome = input("Digite seu primeiro nome: ")
tamanho = len(primeiro_nome)

if tamanho > 1:
    if(tamanho <= 4):
        print("Seu nome é curto")
    elif (tamanho == 5 or tamanho == 6):
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite um nome válido")
