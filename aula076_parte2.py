# Manipulando chaves e valores em dicionários - Aula 120

pessoa = {
    'nome': 'Ana Caroline',
    'sobrenome': 'Bento',
    'idade': 18,
    'altura': 1.6,
    'enderecos':[
        {'rua': 'aaaaaaaaaaa', 'número': 456},
        {'rua': 'desespero', 'número': 789}
    ]
}

# para acessar um item do dicionário, é preciso chamar pelas chaves
print(pessoa['nome']) # estou chamando o item cujo índice é a palavra 'nome'

# é possível definir um dicionário que será 'povoado' posteriormente
pessoa = {}

pessoa['nome'] = 'Caroline' # estou definindo uma nova chave(índice), chamado 'nome', e um valor dentro deste
print(pessoa['nome'])

# é possível criar chaves dinamicamente

chave = 'sobrenome'
pessoa[chave] = 'Bento'
print(pessoa)

# mudando o valor da chave 
pessoa[chave] = 'Santos'
print(pessoa)

# adicionando novas chaves mudando o valor da variável:
chave = 'idade'
pessoa[chave] = 19
print(pessoa)

# da mesma forma, é possível deletar uma chave

del pessoa[chave]
print(pessoa)

# tentar acessar um índice que não existe em um dicionário fará com que o python mostre uma exceção (erro)
# e esse erro fará o programa parar de ser executado 
# nada funcionará depois da exceção
# ainda que a mesma esteja em um if, ele não executará depois dela

# uma das formas de contornar o problema seria utilizando o método get() dos dict
print(pessoa.get('idade', None)) # ele por padrão retorna 'None'
print(pessoa.get('nome', None)) # pode ser usado em IFs

if pessoa.get('idade') is None:
    print('Não Existe')
else:
    print(pessoa['idade'])
