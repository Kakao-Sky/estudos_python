# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *args (n° ilimitado de argumentos posicionais)
# **kwargs (n° ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️posicional.
# PEP 570 - Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - *sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 - Python Positional-Only Parameters
# https://peps.python.org/pep-3102/

def soma(*args):
    print(sum(args))

soma(1)
soma(1, 2, 3)
soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

def outra_soma(a, b, /, x, y):
    print(a + b + x + y)

outra_soma(9, 8, y=7, x=4)

def mais_uma_soma(a, b, *, c):
    print(a + b + c)

mais_uma_soma(3, 4, c=6)