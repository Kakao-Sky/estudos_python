"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
     append - adiciona um item ao final da lista
     insert - adiciona um item no índice escolhido
     pop - remove o item do final da lista ou do índice escolhido
     del - apaga um índice
     clear - limpa a lista
     extend - estende a lista
     + - concatena listas
Create, Read, Update, Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)

"""

# INTRODUÇÃO AO TIPO LIST
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres
lista = [] # ''
print(bool(lista)) # falsy

#         0    1        2         3    4
#        -5   -4       -3        -2   -1
lista = [123, True, 'Carroline', 5.2, []]
print(lista)
print(lista[-3])
print(lista[2], type(lista[2]))

lista[2] = 'Jojo'
print(lista)
print(lista[2], type(lista[2]))

####################################################################
# ALTERANDO UMA LISTA COM ÍNDICES, DEL, APPEND E POP
lista_2 = [10, 20, 30, 40]
lista_2[1] = 300    # mudando um valor na lista
print(lista_2)
del lista_2[2] # deleta um dado independente do índice, e pega os valores posteriores e traz pra antes
print(lista_2)
lista_2.append(50) # adiciona um valor ao fim da lista
print(lista_2)
lista_2.pop() # remove o último valor da lista, no caso, o 50
lista_2.append(60) # adiciona um valor ao fim da lista
lista_2.append(70) # adiciona um valor ao fim da lista
ultimo_valor = lista_2.pop()
print(lista_2, 'removido: ', ultimo_valor)
lista_2.pop(3) # removendo por índice
print(lista_2)

##################################################################################################
# INSERINDO ITENS EM QUALQUER ÍNDICE DA LISTA COM INSERT

#           0   1   2   3
lista_3 = [10, 20, 30, 40]
lista_3.append('Carroline')
nome = lista_3.pop()
lista_3.append(1233)
del lista_3[-1]
# lista_3.clear()
lista_3.insert(0, 5) # dois parâmetros: índice(0), valor(5)
print(lista_3)


###############################################################################################
# ESTENDENDO E CONCATENANDO LISTAS

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # concatenação

print(lista_c)

lista_a.extend(lista_b) # não retorna um valor, portanto, não pode colocar em outra variável(lista)
# é uma ação que ocorre dentro da própria lista_a
print(lista_a)

################################################################################################
"""
Cuidados com os dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

"""
nome = 'Carroline' # a var aponta para o lugar da memória que guarda 'Carroline'
noutra_variavel = nome # copia o dado que tem em nome
nome = 'Karro' # aponta para um lugar diferente da memória

print(nome)
print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1.2, True]
lista_b = lista_a # faz as duas listas apontarem para o mesmo lugar na memória
lista_c = lista_a.copy() # copia o conteúdo da lista

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_c)
