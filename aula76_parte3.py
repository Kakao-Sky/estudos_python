# Métodos úteis dos dicionários em Python
#   len - quantidade de chaves**
#   keys - iterável com as chaves
#   values - iterável com os valores
#   items - iterável com chaves e valores
#   setdefault - adiciona valor se a chave não existe
#   copy - retorna uma cópia rasa (shallow copy)
#   get - obtém uma chave
#   pop - apaga um item com a chave especificada (del)
#   popitem - apaga o último item adicionado
#   update - atualiza um dicionário com outro

# tudo é um objeto em python, inclusive dicionário, por isso tem seus métodos

pessoa = {
    'nome': 'Caroline',
    'sobrenome': 'Bento'
}

print(len(pessoa)) # ** len() é a função que chama o método thunder __len__
# método thunder são aqueles que os nomes começam com 2 underlines antes do nome e 2 depois

print(pessoa.keys()) # retorna as chaves em algo parecido com uma lista ou tupla - pode-se fazer coerção 
print(list(pessoa.keys()))  
print(tuple(pessoa.keys())) 

for chaves in pessoa.keys():
    print(chaves, 'for')

print(pessoa.values()) # retorna os valores em algo parecido com uma lista ou tupla - pode-se fazer coerção 
print(list(pessoa.values()))  
print(tuple(pessoa.values()))

for valor in pessoa.values():
    print(valor, 'for')

print(pessoa.items()) # retorna as chaves e os valores em algo parecido com uma lista ou 
#tupla - pode-se fazer coerção 
print(list(pessoa.items()))  
print(tuple(pessoa.items())) 

for chaves, valores in pessoa.items(): # como o método enumerate para listas
    print(chaves, '|', valores, 'for')

# Para caso alguém solicite uma chave que não existe, é possível configurar um valor 
# padrão para essa chave, com o setdefault

#pessoa.setdefault('idade', 5) # caso não exista essa chave, ele retorna 5
""" pessoa.setdefault('idade', 1) # caso não exista essa chave, ele retorna None
print(pessoa['idade']) """

