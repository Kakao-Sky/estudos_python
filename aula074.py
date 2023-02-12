# Closure e funções que retornam outras funções

def criar_saudacao(saudacao): # cria e chama a execução da função saudar()
    def saudar(nome):
        return f'{saudacao}, {nome}' # retorna o valor criado na execução da função saudar()
    # retorna o local da memória para acessar a função saudar()
    return saudar # retirando os parênteses, ele não vai mais retornar o retorno da função,
    # e sim retornar a função em si, para que esta possa retornar algo posteriormente

# passando parâmetros que serão salvos na função criar_saudacao();
# e que serão utilizados na função saudar(), cujas referências serão salvas nas variáveis abaixo
# e elas poderão ser executadas como se fossem a função
# Closure ^
falar_bom_dia = criar_saudacao('Bom dia') # chama a função criar_saudacao()
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Carol')) # já que as variáveis conseguem referenciar a função, 
#   elas podem ser utilizadas para executar a mesma
print(falar_boa_tarde('Luiza'))

for nome in ['Maria', 'Luiz', 'João']:
    print(falar_boa_noite(nome))
