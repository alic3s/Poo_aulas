import math

class Cilindro:
    def __init__(self, raio, altura) -> None:
        self.raio = raio
        self.altura = altura
    
    def calculaArea(self):
        area = 2 * math.pi * self.raio(self.altura + self.raio)
        return area
        
        
    def calculaVolume(self): 
        return math.pi * math.pow(self.raio, 2) * self.altura
        
    def __str__(self):
        return f'Area: {self.calculaArea}\nVolume: {self.calculaVolume}'
