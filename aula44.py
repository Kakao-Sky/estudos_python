# For + Range
# range -> range(start, stop, step) / (início, fim, passo)
# Range -> números

# Se apenas um número for passado, esse número significa apenas o stop, tendo 0 como start e 1 como step
numeros = range(10)
print(numeros)
numeros = range(5, 10)
print(numeros)
numeros = range(5, 10, 2)
print(numeros)

numeros = range(10)
for numero in numeros:
    print(numero)