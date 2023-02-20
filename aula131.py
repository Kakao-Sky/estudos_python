# @property - um getter no modo Pythônico
# getter - método para obter um atributo
# modo pythônico -> modo do Python de fazer coisas
# @property -> é uma propriedade do objeto; é um método que se comporta como um atributo
# Geralmente usado nas seguintes situações:
#   - como getter;
#   - p/ evitar quebrar código cliente
#   - p/ habilitar setter
#   - p/ executar ações ao obter um atributo

# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         print('GET')
#         return self.cor

# caneta = Caneta('azul')

# print(caneta.cor)
# print(caneta.get_cor())


#########################################################################################################


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123

caneta = Caneta('azul')
print(caneta.cor)
print(caneta.cor_tampa)
# cor -> método que se comporta como atributo
