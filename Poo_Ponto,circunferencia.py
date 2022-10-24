class Ponto:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
    
    def alterar_cor(self, nova_cor = ''):
       self.cor = nova_cor
    
    def __str__ (self):
        return f' Esse é meu objeto: [{self.x}, {self.y}, {self.cor}]'

class Circunferencia:
    def __init__(self, ponto, raio, cor_linha, cor_preenchimento):
        self.raio = raio
        self.cor_linha = cor_linha
        self.cor_preenchimento = cor_preenchimento
        self.centro = ponto
    
    def area(self):
        return 3.14 * (self.raio**2)

    def perimetro(self):
        return 2 * (3.14 * self.raio)
    
    def __str__ (self):
        return f' Esse é meu objeto: [{self.centro}, {self.raio}, {self.cor_linha}, {self.cor_preenchimento}]'

p1 = Ponto(1, 2, 'branco')
p2 = Ponto(3, 4, 'preto')

p1.alterar_cor('Lilás')
print(p1)

c1 = Circunferencia(p1.y, 3, 'azul', 'roxo')
print(c1.area())
print(c1.perimetro())
print(c1)
