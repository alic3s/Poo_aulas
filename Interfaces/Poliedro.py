class Poliedro:
    def __init__(self, qtdVertice, qtdAresta, qtdFace, lado1, lado2, altura):
        self.qtdVertice = qtdVertice
        self.qtdAresta = qtdAresta
        self.qtdFace = qtdFace
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura

    def ehconvexo(self):
        if self.qtdVertice - self.qtdAresta + self.qtdFace == 2:
            return True
        else:
            return False

    def __str__(self):
        if self.ehconvexo():
            poliedro é convexo
        else:
            nao é convexo
        return f'Area: {self.calculaArea}\nVolume: {self.calculaVolume}'
