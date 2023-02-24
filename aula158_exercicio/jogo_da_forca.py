from jogos import Jogo
import random

class JogoDaForca(Jogo):
    def __init__(self, nome, palavras):
        super().__init__(nome, palavras)
        self.palavra_secreta = ''
    
    def tornar_palavra_secreta(self):
        for letra in self.palavra_escolhida:
            ...

    def verificar_letra(self, letra):
        self.pegar_palavras()
        self.escolher_palavra()
        print(self.palavra_escolhida)

    
jogo_1 = JogoDaForca('Forca', ['paralelepípedo', 'ornitorrinco', 'mamífero', 'catavento'])
jogo_1.salvar_palavras()

