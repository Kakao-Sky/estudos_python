# Gerador de CPFs válidos

import random # importando random, para pegar números aleatórios

cpf_gerado_9d = [] # lista que guardará os primeiros nove números

# Colocando nove primeiros números do CPF na lista
for numero in range(9):
    cpf_gerado_9d.append(random.randint(0, 9))

# Salvando a multiplicação individual dos primeiros 9 números
multiplicacao_individual_9p = [] 
indice = 0
contador_regressivo_1 = 10
while indice <= 8:
    multiplicacao_individual_9p.append(cpf_gerado_9d[indice] * contador_regressivo_1)
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

# Calculando segundo dígito
cpf_gerado_10d = [] # lista que guardará os 10 dígitos
cpf_gerado_10d = cpf_gerado_9d.copy() # copiando os 9 dígitos gerados
cpf_gerado_10d.append(primeiro_digito) # incluindo o primeiro dígito

# Multiplicação individual de 10 dígitos (9 primeiros + primeiro)
multiplicacao_individual_10d = [] 
indice = 0

contador_regressivo_2 = 11
while indice <= 9:
    multiplicacao_individual_10d.append(cpf_gerado_10d[indice] * contador_regressivo_2)
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

cpf_completo = cpf_gerado_10d.copy()
cpf_completo.append(segundo_digito)

print(cpf_gerado_9d, primeiro_digito)
print(cpf_gerado_10d, segundo_digito)
print(*cpf_completo)

