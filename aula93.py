# Try, except, else e finally

"""try:
    ...
finally:    # funciona assim
    ..."""

# maneira mais comum de utilizar, mas não simplesmente try...except... -> precisa tratar as exceções
a = 18
b = 0
 
try:
    print(b[2])
    print('até aqui executa')
    c = a / b
    print('não executa')
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Você deixou de definir uma variável')
except (TypeError, IndexError) as error: # passando dois erros a serem tratados, passando em uma tupla 
    # "as error" -> pega a mensagem do erro que deu, já que dois estão sendo tratados e colocando na var "error"
    print('Erro de tipo ou erro de índice')
    print('MSG: ', error)
    print('Nome do erro: ', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('Código continuando normalmente')