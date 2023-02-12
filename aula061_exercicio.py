"""
Exercício - Calculando o primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
multiplicando cada um dos valores por uma contagem regressiva começando de 10


Ex.: 746.824.890-70 (743824890)
   10  9  8  7  6  5  4  3  2  
   7   4  6  8  2  4  8  9  0 
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado por 10:
301 * 10 = 3010
Obter o resto da divisão por 11:
3010 % 11 = 7
Se o resto é maior que 9:
    resultado = 0
contrário disso:
    resultado = resto

o primeiro do CPF é 7
"""

# MINHA SOLUÇÃO -> só funcionou com o cpf que ele deu :/ 

#cpf_string = '746.824.890-70' # testando com o valor dado, para verificar
cpf_string = input('Digite seu CPF: ')
cpf_int = []

# Extraindo somente os números do CPF
for caracter in cpf_string:
    if caracter.isdigit():
        cpf_int.append(int(caracter))

print(*cpf_int)

# Salvando a multiplicação individual dos primeiros 9 números
multiplicacao_individual_9p = [] 
indice = 0
contador_regressivo_1 = 10

""" multiplicacao_individual_9p.append(cpf_int[indice] * contador_regressivo_1)
print(multiplicacao_individual_9p) # só um teste """

while indice <= 8:
    multiplicacao_individual_9p.append(cpf_int[indice] * contador_regressivo_1)
    contador_regressivo_1 -= 1
    indice +=1

print(multiplicacao_individual_9p) # só pra verificar se tá correto

# Somando todos os resultados da multiplicação
soma_multi_individual_9p = 0

for numero in multiplicacao_individual_9p:
    soma_multi_individual_9p += numero

print(soma_multi_individual_9p)

# Realizando a multiplicação da soma por 10
multiplicacao_soma = soma_multi_individual_9p * 10
print(multiplicacao_soma)

# Resto da divisão por 11
resto_divisao = multiplicacao_soma % 11
print(resto_divisao)

# Verificação de validação
primeiro_digito = 0
if (resto_divisao > 9):
    primeiro_digito = 0
else:
    primeiro_digito = resto_divisao

print(f'O primeiro dígito é: {primeiro_digito}')


# Solução do PROFESSOR - primeiro dígito

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
