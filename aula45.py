# Como funciona (next, iter, iterável e iterador)
# Iterável -> str, range, etc
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

texto = 'Luiz'
iterador = iter(texto) # __iter__()

# basicamente, o for faz isso:
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

""" print(texto)
print(texto.__next__()) # next()
print(texto.__next__())
print(texto.__next__())
print(texto.__next__()) # esse é o último valor
 """# após acabarem os valores, ele retorna um erro, e o for reconhece isso 



numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)