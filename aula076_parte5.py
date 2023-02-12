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

p1 = {
    'nome': 'Carol',
    'sobrenome': 'Bento',

}

""" nome = p1.pop('nome')
print(nome, p1) """

""" ultima_chave = p1.popitem()
print(ultima_chave)
print(p1) """

print(p1)
""" p1.update({
    'nome': 'novo nome',
    'idade': 30,
})
print(p1) """

""" p1.update(nome='Ana', idade=20)
print(p1) """

tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
#p1.update(tupla) # pode receber um iterável que se comporta como dicionário 
print(p1)
