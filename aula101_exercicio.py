# Exercício - Adiand execução de funções 

def soma(x, y): # a função soma requer a passagem de dois argumentos
    return x + y

def multiplica(x, y): # a função multiplica requer a passagem de dois argumentos
    return x * y

"""def executa(funcao, *args): # essa função requer a passagem de uma função como argumento, e outros argumentos que a função requerir
    return funcao(*args) # escrito dessa forma vai dar erro, pois vai tentar executar assim que for chamada, para pausar,
    #é preciso não executar logo de cara"""

# Solução
def executa(funcao, x): # agora a função executa precisa receber a função a ser execuada e um argumento
    def interna(y): # essa função recebe o segundo argumento necessário
        # a função interna() faz a função de adiar a execução, executando a função passada por parâmetro
        return funcao(x, y) # retorna a execução com os valores necessários
    return interna # retorna a função interna, que requer apenas um parâmetro 
    


# essa varável vai receber a execução da função soma, e repassar um parâmetro pra ela, porém isso vai dar um erro porque requer 2 parâmetros
soma_com_cinco = executa(soma, 5)

multiplica_por_dez = executa(multiplica, 10)

# as variáveis "soma_por_cinco" e "multiplica_por_dez" agora são referenciais pras funções "soma" e "multiplica" dentro da função "executa"
print(soma_com_cinco(9)) # fechamento -> closure
print(multiplica_por_dez(8))
