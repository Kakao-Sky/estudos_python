# a aula 145 é na verdade a aula 119_ultima.py

# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.orgs/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


# devs comunicam erros através de exceções 

# herdando de Exception
class MeuError(Exception): # é uma convenção do Python add "Error" ao final do nome
    ...

class OutroError(Exception): # é uma convenção do Python add "Error" ao final do nome
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    # add_note não funcionou aqui :/
    raise exception_

try:
    levantar()
except MeuError as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error 