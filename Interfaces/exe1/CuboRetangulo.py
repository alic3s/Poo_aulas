import math
from Poliedro import Poliedro

class Cubo(Poliedro):
    def __init__(self, qtdVertice, qtdAresta, qtdFace, lado1):
        Poliedro.__init__(self, qtdVertice, qtdAresta, qtdFace, lado1)
        
    def calculaArea(self):
        print(6 * math.pow(self.lado1, 2))
        return 2 * (self.lado1 + self.lado1 + self.lado1)
        
    def calculaVolume(self):
        return math.pow(self.lado1, 3)


class Retangulo(Poliedro):
    def __init__(self, qtdVertice, qtdAresta, qtdFace, altura, comprimento, largura):
        Poliedro.__init__(self,qtdVertice, qtdAresta, qtdFace)
        self.altura = altura
        self.comprimento = comprimento
        self.largura = largura
    
    def calculaArea(self):
        return 2 * (self.largura * self.comprimento + self.comprimento * self.altura + self.largura * self.comprimento)

    def calculaVolume(self):
        return self.altura * self.comprimento * self.largura
