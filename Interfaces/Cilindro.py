class Cilindro:
    def __init__(self, raio, altura) -> None:
        self.raio = raio
        self.altura = altura
    
    def calculaArea(self):
        return {2 * 3,14 * self.raio(self.altura + self.raio)}
        
    def calculaVolume(self): 
        return {3,14 * self.raio * self.raio * self.altura}
    
    def __str__(self):
        return f'Area: {self.calculaArea}\nVolume: {self.calculaVolume}'
