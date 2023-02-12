# Calculadora com while

while True:

    # recebendo números e operações
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    # Falgs e variáveis auxiliares
    numeros_validos = None # isso é uma flag
    operadores_permitidos = '+-/*'

    # definindo as variáveis fora dos blocos
    num_1_float = 0
    num_2_float = 0

    # verificando se os números são números 
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True # utilizando a flag
    except:
        numeros_validos = None

    # enviando feedback de validação dos números aos usuários
    if numeros_validos is None:
        print('Os números não são válidos')
        continue

    # enviando feedbacks de validação dos operadores aos usuários
    if operador not in operadores_permitidos:
        print('O operador não é válido')
        continue
    if len(operador) > 1:
        print("Digite apenas um operador válido")
        continue

    print("Resultado: ")
    # fazendo tratamento para as operações
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    else:
        print("Algo de errado não está certo")


    # função de saída do código
    sair = input("Você deseja sair? [s]im: ").lower().startswith('s')

    if sair:
        break
