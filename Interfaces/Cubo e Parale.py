from poliedro import Poliedro

class Cubo(Poliedro):
    def __init__(self, qtdVertice, qtdAresta, qtdFace, lado1, lado2, altura, lado):
        super().__init__(qtdVertice, qtdAresta, qtdFace, lado1, lado2, altura)
        self.lado = lado

    def calculaArea(self):
        return 2 * (self.lado + self.lado + self.lado)
    
    def calculaVolume(self):
        return 3 * self.lado
