# Introdução às funções (def) em Python
# Funções são trechos de código usados para replicar 
# determinada ação ao longo do código.
# Elas podem receber valores para parâmetros (argumentos)
#  e retornam um valor específico.
# Por padrão, retornam None (nada)

print('isso é uma função') # a função print() existe no python

# Print() -> esse código está errado, pois Python faz distinção entre letras maiúsculas e minúsculas
# mas pode-se definir uma função com esse nome e chamá-la assim estará correto
# Obs.: não é uma boa prática usar letras iniciais maiúsculas em nomes de funções

# Ex.: 
def Print(): # def nome_da_funcao(): -> define que uma função está sendo criada
    print('Essa função se chama Print(), e agora funciona chamar assim')

Print() # -> chamando a função criada

# parâmetros != argumentos
# parâmetros -> variáveis passadas para a função

def imprimir(a, b, c): # a, b, c -> parâmetros
    print(a, b, c) # blocos de código da função

# argumentos -> valores passados quando a função é chamada
imprimir(1, 2, 3) # 1, 2, 3 -> argumentos
imprimir(4, 8, 3) 

#############################################################################################
def saudacao(nome='Oh, sem nome'): # 'Oh, sem nome é o default
    print(f'Olá, {nome}')

saudacao('Carroline')
saudacao('Helena')
saudacao('Jubiscreudo')
saudacao() 