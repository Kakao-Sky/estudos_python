# @property + @setter -> getter e setter no modo Pythônico
# - como getter
#   - como getter;
#   - p/ evitar quebrar código cliente
#   - p/ habilitar setter 🌈(ainda não visto na aula anterior)
#   - p/ executar ações ao obter um atributo
# Atributos cujos nomes iniciarem com um ou dois underlines não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        # private ou protected:
        self._cor = cor # não deve ser usado fora da classe

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor

    # para ter um setter, precisa de um property (podem ter o mesmo nome)
    @cor.setter # já vem com o nome, por isso precisa do property
    def cor(self, valor): # precisa do acesso ao self, mas precisa de outro valor(p/ setar)
        self._cor = valor

caneta = Caneta('Arco-íris🌈')
# getter -> obter valor
print(caneta.cor) # getter

caneta.cor = 'Rosa 🌷' # setter
print(caneta.cor) # getter
