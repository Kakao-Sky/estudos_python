'''
Iterando Strings com while

'''

### MINHA SOLUÇÃO
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

# print(nome, tamanho_nome)

iterador = 0
novo_nome = '*-*'
while iterador < tamanho_nome:
    print(nome[iterador])
    novo_nome += nome[iterador] + '*-*'
    iterador += 1

print(novo_nome)




### SOLUÇÃO DO PROFESSOR
nome = 'Luiz Otávio'

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
