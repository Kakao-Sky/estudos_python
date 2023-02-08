# Try, except, else e finally

try:
    print('tentando...')
    8/2
except ZeroDivisionError:
    print('Dividiu por zero')
else: # else só vai ser executado se der certo
    print('executa se não deu erro')
finally: # o finally sempre vai ser executado, mesmo que o try... tenha sido bem resolvido
    print('deu ruim') # sempre vai ser executado, mesmo que dê erro

############################################################################################################################################################

try:
    print('tentando...')
    8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('executa se não deu erro')
finally: # o finally sempre vai ser executado, mesmo que o try... tenha sido bem resolvido
    print('deu ruim') # sempre vai ser executado, mesmo que dê erro

# try.. não pode ficar sozinho
# except... não pode ficar sozinho
# try...except funciona
# try...finally... funciona