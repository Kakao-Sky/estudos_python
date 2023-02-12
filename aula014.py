a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f}' #a quantidade de {} deve ser compatível com a quantidade de args
#o valor dentro das {} pode ser pegado por índices

formato = string.format(a, b, c)
print(formato)

string_2 = 'a={2} b={1} c={0}'
formato = string_2.format(a, b, c)
print(formato)

# é possível nomear os args, então, serão chamados de parâmetros
string_3 = 'a={var2} b={var1} c={var3}'
#após um parâmetro ser nomeado, todos depois dele deverão ser nomeados também
formato = string_3.format(var1=a, var2=b, var3=c) 
print(formato)

