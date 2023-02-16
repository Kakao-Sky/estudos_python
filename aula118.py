# Problemas dos parâmetros mutáveis em funções Python

# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# uma forma de resolver
def adiciona_clientes(nome, lista=None):
    if lista is None: # se nenhum argumento for repassado neste parâmetro
        lista = []
    lista.append(nome)
    return lista

# cliente1 = adiciona_clientes('luiz')
# adiciona_clientes('joana', cliente1)
# print(cliente1)

# # problema: a lista vai ser carregada na chamada da função, e todas as vezes em que a função for chamada, a lista já vai estar carregada
# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente2)

# uma forma de resolver seria você mesmo ter sua lista e repassar na primeira chamada da função
# o que faria a lista que está como parâmetro da função não ser mais chamada junto a ela

lista1 = []
cliente1 = adiciona_clientes('luiz', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1)

# agora formam listas diferentes
cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Carol')
adiciona_clientes('Vivi', cliente3)
print(cliente3)

# Observações: é recomendado não usar parâmetros mutáveis em funções (lists, dict, sets), mas se for o caso de precisar usar,
# é recomendado não definir um valor padrão (tipo uma lista vazia), é preferível usar None (nada) 
