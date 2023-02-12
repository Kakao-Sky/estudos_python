"""
Exercício - Calculando o segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DÍGITO
multiplicando cada um dos valores por uma contagem regressiva começando de 11



Ex.: 746.824.890-70 (743824890)
   11 10  9  8  7  6  5  4  3  2  
   7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DÍGITO
   77  40 54 64 14 24 40 36 0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado por 10:
363 * 10 = 3630
Obter o resto da divisão por 11:
3630 % 11 = 0
Se o resto é maior que 9:
    resultado = 0
contrário disso:
    resultado = resto

"""

# para fazer esse código, precisa do código do primeiro dígito
#cpf_string = '746.824.890-70' # testando com o valor dado, para verificar
cpf_string = input('Digite seu CPF: ')
cpf_int = []

# Extraindo somente os números do CPF
for caracter in cpf_string:
    if caracter.isdigit():
        cpf_int.append(int(caracter))

# Salvando a multiplicação individual dos primeiros 9 números
multiplicacao_individual_9p = [] 
indice = 0
contador_regressivo_1 = 10
while indice <= 8:
    multiplicacao_individual_9p.append(cpf_int[indice] * contador_regressivo_1)
    contador_regressivo_1 -= 1
    indice +=1

# Somando todos os resultados da multiplicação
soma_multi_individual_9p = 0
for numero in multiplicacao_individual_9p:
    soma_multi_individual_9p += numero

# Realizando a multiplicação da soma por 10
multiplicacao_soma = soma_multi_individual_9p * 10

# Resto da divisão por 11
resto_divisao = multiplicacao_soma % 11

# Verificação de validação
primeiro_digito = 0
if (resto_divisao > 9):
    primeiro_digito = 0
else:
    primeiro_digito = resto_divisao

# CÓDIGO PRO SEGUNDO DÍGITO (MINHA solução)

# Multiplicação individual de 10 dígitos (9 primeiros + primeiro)
multiplicacao_individual_10d = [] 
indice = 0
contador_regressivo_2 = 11
while indice <= 9:
    multiplicacao_individual_10d.append(cpf_int[indice] * contador_regressivo_2)
    contador_regressivo_2 -= 1
    indice +=1

# Somando todos os resultados da multiplicação
soma_multi_individual_10d = 0
for numero in multiplicacao_individual_10d:
    soma_multi_individual_10d += numero

# Multiplicando a soma por 10
multiplicacao_soma_2 = soma_multi_individual_10d * 10

# Pegando o resto da divisão por 11
resto_divisao_2 = multiplicacao_soma_2 % 11

# Verificação de validação
segundo_digito = 0
if (resto_divisao_2 > 9):
    segundo_digito = 0
else:
    segundo_digito = resto_divisao_2

if(primeiro_digito == cpf_int[9] and segundo_digito == cpf_int[10]):
    print('CPF válido')
else:
    print('CPF inválido')
print(f'O segundo dígito é: {segundo_digito}')



###############################################################################################
# solução do PROFESSOR 

# primeiro dígito
cpf = '74682489070'
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
