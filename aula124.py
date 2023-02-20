# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando is True:
            print(f'{self.nome} já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True # está guardando o estado 
    
    def parar_de_filmar(self):
        if self.filmando is not True:
            print(f'{self.nome} já não está filmando...')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} está filmando, não pode fotografar')
            return
        print(f'{self.nome} está fotografando')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.parar_de_filmar()
c1.fotografar()
print()
c2.fotografar()
c2.filmar()
c2.parar_de_filmar()
c2.fotografar()
c2.filmar()
# print(c1.filmando) # estão guardando os estados das coisas
# print(c2.filmando)

