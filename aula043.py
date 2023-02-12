# Introdução ao for / in - estrutura de repetição para coisas finitas
# while -> para coisas finitas ou infinitas

texto = 'Python'

# while para iterar a string:
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1
# Não é comum utilizar o while com coisas que se sabe onde terminam

# Iteração com o for:
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
