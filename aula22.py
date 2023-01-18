# Operadores Lógicos
# and (e), or (ou), not (não)
# or - Qualquer condição verdadeira avalia a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy (0, 0.0, '', False, dentre outros)
# Também existe o None, usado para representar um Não-Valor

entrada = input('[E]ntrar | [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print("Entrar")
else: 
    print('Sair')
print(entrada)

# Avaliação de curto circuito
print(True or False)
print(True or False or 0)
print(0 or False or 0.0 or 'abc') # 'abc' é considerado o primeiro valor verdadeiro
print('aaa' or True or False or 0.0 or 'abc')
