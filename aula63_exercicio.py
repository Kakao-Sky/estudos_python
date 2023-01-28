# Possíveis problemas encontrados no código do CPF:

# A pessoa enviar o CPF como normalmente 746.824.890-70
# Meu código não permitia esse erro, mas o do professor sim
# nesse caso, utilizou o método replace()

# solução do PROFESSOR 
import re # para usar expressões regulares
import sys
# primeiro dígito

# replace -> indica o que será mudado e o que vem no lugar
#cpf = '746.824.890-70'.replace('.', '').replace('-', '') 

# também é possível solucionar com expressões regulares
cpf = re.sub(r'[^0-9]', '', '746.824.890-70') # tudo o que não for número, substitua para nada

# não permitindo que o usuário só repita os números:
repeticao = cpf == cpf[0] * len(cpf)
if repeticao:
    print('Cpf inválido')
    sys.exit() # mata o processo aqui mesmo

nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1 
    contador_regressivo_1 -= 1 
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

# segundo dígito

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2 
    contador_regressivo_2 -= 1 
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

# validação
novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

print(novo_cpf)

if novo_cpf == cpf:
    print(f'O CPF {cpf} é válido')
else:
    print(f'O CPF {cpf} não é válido')
