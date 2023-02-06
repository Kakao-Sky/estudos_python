# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s2 = {1, 2, 3, 3, 3, 3, 3, 1, 4} # vai eliminar automaticamente a repetição
print(s2)

l1 = ['a', 'b', 'c', 'd', 'e', 'a']
s3 = set(l1) 
print(s3)



# Métodos úteis:
# add, update, clear, discard

s4 = set()
s4.add('Carol') # adicionar um valor ao set
print(s4)

s4.update('olá mundo') # coloca cada valor desse iterável separadamente
print(s4)

s4.update(('Olá, mundo', 1, 2, 3)) # pode-se colocar uma tupla dentro dele
print(s4)

s4.discard('Olá, mundo') # elimina o valor especificado
s4.discard('Carol')
print(s4)

s4.clear() # limpa todo o set
print(s4)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # une os dois conjuntos
s4 = s1 & s2 # mostra a intersecção deles
s5 = s1 - s2 # mostra a diferença entre eles
s6 = s1 ^ s2 # mostra a diferença simétrica deles

print(s3)
print(s4)
print(s5)
print(s6)
