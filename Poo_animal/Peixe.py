from animal import Animal

class Peixe(Animal):
    def __init__(self, nome, comprimento, patas, cor, ambiente, velocidade, caracteristica):
        super(). __init__(nome, comprimento, patas, cor, ambiente, velocidade)
        self.caracteristica = caracteristica
    
    def dadosPeixe(self):
        super().dados()
        print(f'Característica: {self.caracteristica}')


peixe = Peixe('Xuxu', 12.4, 0, 'Laranja', 'Água', 20.5, 'Listrado')
