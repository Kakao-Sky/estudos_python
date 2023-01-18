# Operadores Lógicos
# and (e), or (ou), not (não)
# and - Todas as condições precisam ser VERDADEIRAS
# Se qualquer valor for falso, toda a expressão será
# São considerados falsy (0, 0.0, '', False, dentre outros)
# Também existe o None, usado para representar um Não-Valor

#if 0 and 1: - terá como retorno 0, nada
 #   print(True and 1) - não será executado


entrada = input('[E]ntrar | [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print("Entrar")
else: 
    print('Sair')
print(entrada)

# Avaliação de curto circuito
print (True and False and True) # a avaliação acaba no valor falso
print (True and 0 and True) # se ele encontrar qualquer valor que considere um bool falso, ele será o valor da expressão
print(bool(0))
print(bool(0.0))