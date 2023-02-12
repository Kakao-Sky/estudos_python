# Minha solução
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if(primeiro_valor > segundo_valor):
    print(f'O {primeiro_valor=} é maior que o {segundo_valor=}')
elif(segundo_valor > primeiro_valor):
    print(f'O {segundo_valor=} é maior que o {primeiro_valor=}')
else:
    print(f'Ambos os valores, {primeiro_valor=} e {segundo_valor=} são iguais')

# Solução do professor

if(primeiro_valor >= segundo_valor):
    print(f'O {primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'O {segundo_valor=} é maior que o {primeiro_valor=}')
