from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, comprimento, patas, cor, ambiente, velocidade, alimento):
        super().__init__(nome, comprimento, patas, cor, ambiente, velocidade)
        self.alimento = alimento
    
    def dadosMamifero(self):
        super().dados()
        print(f'Alimento: {self.alimento}')
