# slpit e join com list e str
# split -> divide uma string
# join -> une uma string
# strip -> corta os espaços presentes no início e no fim da string

frase = "Olha só, que coisa interessante"
lista_palavras_crua = frase.split() # sem nenhum parâmetro, ele vai separar pelos espaços em branco e quebra de linha
print(lista_palavras_crua)

lista_palavras_crua = frase.split(',') # estou indicando que quero que divida na vírgula
print(lista_palavras_crua)

# após indicar o que eu quero que corte a frase (','), eu uso um for para passar pela lista criada
# e escrevê-la, retirando os espaços 

lista_frase = [] # boa prática -> criar uma lista nova, pra poder alterar e ainda salvar o valor antigo
for i, frase in enumerate(lista_palavras_crua):
    # alterando a lista
    lista_frase.append(lista_palavras_crua[i].strip())

print(lista_palavras_crua)
print(lista_frase)

lista_palavras_crua = frase.split('a') # pode-se usar outro caracter
print(lista_palavras_crua)



#####################################################################################################
# FALANDO SOBRE O join

# '-' é o separador que será colocado entre os iteráveis
# 'abc' é uma str, ou seja, um iterável
frases_unidas = '-'.join('abc')
print(frases_unidas)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)

frases_unidas = '-'.join('uma frase é uma string, um iterável cheio de itens')
print(frases_unidas)
