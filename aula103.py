# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o python usar as funções decoradoras em outras funções


# ESSA É A FUNÇÃO DECORADORA:
def criar_funcao(func): # recebe uma função como arg/parâmetro
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            checa_str(arg)
        resultado = func(*args, **kwargs)
        print(f'seu resultado foi {resultado}')
        print('Ok, decorado')
        return resultado
    
    return interna # retorna sem ser executada


#####
def inverte_str(string):
    return string[::-1]
#####
def checa_str(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

inverte_str_checando_param = criar_funcao(inverte_str)
invertida = inverte_str_checando_param('Carol')
print(invertida)

# princípio da responsabilidade única -> um objeto deve fazer somente uma coisa,
#  se tiver mais de uma função, deve ser dividido em mais objetos

