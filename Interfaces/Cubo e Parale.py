from poliedro import Poliedro

class Cubo(Poliedro):
    def __init__(self, qtdVertice, qtdAresta, qtdFace, lado1):
        Poliedro.__init__(qtdVertice, qtdAresta, qtdFace, lado1, lado1, lado1)
        
    def calculaArea(self):
        return 2 * (self.lado + self.lado + self.lado)
        6 * math.pow(self.lado1, 2)
    
    def calculaVolume(self):
        return 3 * self.lado
