# Recarregando módulos, importlib e singleton
# Um módulo python é singleton
# singleton -> significa que só pode existir uma instância dele no programa inteiro
# mas é possível recarregar esse módulo com a importlib

import importlib
import aula98_m

print(aula98_m.variavel)

for i in range(10):
    print(i)
    import aula98_m # não acontece nada, por ele ser singleton
    importlib.reload(aula98_m)


