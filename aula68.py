# Escopo de funções em Python
# Escopo: significa o local onde aquele código pode atingir.
# Existe ESCOPO GLOBAL e LOCAL.
# o Escopo Global: é o escopo onde todo o código é alcançável.
# o Escopo Local: é o escopo onde apenas nomes do mesmo local podem ser alcançados. 

def escopo():
    x = 1 # se a variável x fosse definida fora da função, mas antes dela, funcionaria sem problemas
    print(x)


escopo() # se x fosse definido depois de chamar a função, daria algum erro, por não existir a variável no momento em que foi chamada

# isso considerando que x não fosse declarado dentro da função

# Exemplo:
y = 9 # está no escopo global

def funcao():
    y = 8 
    def outrafuncao():
        global y
        z = 10
        print(y, z, 'aqui peguei o valor do y global, definido fora da fun') # o y pode ser acessado aqui, ele vai pegar a variável que tem esse nome que estiver no escopo mais próximo
    
    outrafuncao() # a funcao() chama outra função que foi definida dentro dela
    print(y, 'valor de y local') # eu consigo acessar o valor de y pq ele foi declarado no escopo do módulo python (código do arquivo)

print(y)
funcao()
print(y)

