# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html

# inteiro - import nome_modulo
# Vantagens: ter o namespace do módulo
# Desvantagens: nomes grandes

"""import sys
 
# seria possível ter uma variável 'platform'
print(sys.platform) # "sys" - namespace do módulo - nome grande para chamar """


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: sem o namespace do módulo

"""from sys import exit, platform
# não é mais possível ter a variável 'platform'
print(platform)
"""

# alias 1 - import nome_modulo as apelido
"""import sys as s 

sys = 'alguma coisa' # se a var tiver o mesmo nome de algo importado, a variável vai sobrescrever isso
print(sys)
print(s.platform)"""

# alias 2 - from nome_modulo import objeto as apelido
"""from sys import platform as p, exit as ex

print(p)"""

# Vantagens: você pode reservar nomes para seu codigo
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *

print(platform)

# funciona para importação dos módulos padrão do Python, mas também funciona para a importação dos módulos que você mesmo criou