# Para importar algo dentro deste módulo é importante pensar nos lugares em que este módulo será usado
# do ponto de vista do __main__, pode ser que algum outro módulo importado aqui não existe pra ele
# por isso, é sempre bom importar algo do ponto de vista do __main__

#from modulo_b import fala_oi # fazendo a importação sem levar em consideração o __main__
from aula99_package.modulo_b import fala_oi # fazendo a importação levando em consideração o __main__

def soma_do_modulo(x, y):
    return x + y

fala_oi()
