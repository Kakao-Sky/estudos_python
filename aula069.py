# Passando no debugger
# Escopo de funções em Python
# Escopo: significa o local onde aquele código pode atingir.
# Existe ESCOPO GLOBAL e LOCAL.
# o Escopo Global: é o escopo onde todo o código é alcançável.
# o Escopo Local: é o escopo onde apenas nomes do mesmo local podem ser alcançados. 
# Não temos acesso a nomes de escopos internos nos escopos externos.
#   Ex.: uma var definida somente dentro da função, não é acessada de fora da função.
# A palavra 'global' faz uma variável do escopo externo ser a mesma utilizada no escopo interno
# (dentro da função).

x = 1 # escopo externo

def escopo():
    # global x # acessando variável do escopo externo dentro da função escopo()
    x = 10 # essa variável x é interna da função escopo()

    def outra_funcao():
        # global x -> não é uma boa prática
        x = 11 # essa variável x é interna da função outra_funcao()
        y = 2
        print(x, y)
    
    outra_funcao() # função escopo() chamando a função outra_funcao()
    print(x)

print(x)
escopo()
print(x)

# as chamadas às variáveis dentro dos escopos vão pegar os valores mais próximos, 
# caso não seja definido se é global
