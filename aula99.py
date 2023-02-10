# Introdução aos packages
# importar somente um package não vai alterar nada no programa

# esse é o meu __main__

#from sys import path
"""print(*path, sep='\n') # mostrando os caminhos de arquivos do main
print(__name__)"""

# import aula99_package.modulo # 2° forma
# from aula99_package import modulo # 3° forma
# from aula99_package.modulo import soma_do_modulo # 1° forma


# print(soma_do_modulo(4, 3))# 1° forma
# print(aula99_package.modulo.soma_do_modulo(9, 8)) # 2° forma
# print(modulo.soma_do_modulo(5, 3)) # 3° forma

# modulo.fala_oi()

############################################################################################################
# aula 159

import aula99_package # por causa do __init__ tá se comportando como um módulo
# print(aula99_package.dobra(2))

print(aula99_package.soma_do_modulo(7, 8))
