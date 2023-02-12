# Higher Order Functions 
# Funções de primeira classe 

def saudacao(msg, nome): # essa função precisa receber um argumento
    return f'{msg}, {nome},'

#print(saudacao('Bom dia'))

# saudacao_2 = saudacao # são a mesma cosa, apontam pro mesmo lugar na memória

def executa(funcao, *args): # essa função precisa de 2 args, o nome de outra função, e o arg que a outra função precisa
   # empacota e desempacota os argumentos pra função que tá sendo chamada
    return funcao(*args)

v = executa(saudacao, 'AAAAAAAA', 'carroline') # essa variável recebe o retorno da função, que recebe o retorno de outra função
print(v)

# Moral da história: funções são um tipo de dado em python, que podem ser repassadas 
# como variáveis para outras funções - first-class functions
