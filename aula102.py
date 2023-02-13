# Variáveis livres + nonlocal (locals, globals - funções que dizem se a var é livre ou não)
#print(globals()) # mostra todas as variáveis globais contidas aqui
# def fora(x):
#     a = x # "a" está na função fora, então é uma variável livre
    
#     def dentro():
#         print(locals()) # vai mostrar as variáveis que são locais dentro do escopo dessa função
#         print(dentro.__code__.co_freevars) # mostra as variáveis que são livres
#         return a
#     return dentro

# dentro1 = fora(10) # closure
# dentro2 = fora(20) # closure

# print(dentro1())
# print(dentro2())

def concatenar(str_inicial):
    valor_final = str_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # vai fazer o python buscar essa var em um outro lugar
        valor_final += valor_a_concatenar # isso vai gerar um erro, pois essa freevar só pode ser lida, não modificada (caso não use nonlocal)
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)