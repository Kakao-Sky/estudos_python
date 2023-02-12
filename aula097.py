# Modularização - Entendendo seus próprios módulos em Python
# O primeiro módulo executado se chama '__main__'
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path 
import sys

# sys.path.append('/caminho') -> indica um caminho fora dessa pasta onde você tem módulos python

import aula97_m

print('Este módulo se chama', __name__)
#print(*sys.path, sep='\n')

############################################################################################################################################################
############################################################################################################################################################

# seu __main__ é ponto de entrada 
print(aula97_m.variavel_modulo)

print(aula97_m.soma(2, 3))
