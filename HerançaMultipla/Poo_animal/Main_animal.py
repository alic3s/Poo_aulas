class Animal:
    def __init__(self, nome, comprimento, patas, cor, ambiente, velocidade):
        self.nome = nome
        self.comprimento = comprimento
        self.patas = patas
        self.cor = cor
        self.ambiente = ambiente
        self.velocidade = velocidade
    
    def dados(self):
        print(f'Nome: {self.nome}\nComprimento: {self.comprimento}\nNúmero de patas: {self.patas}\nCor: {self.cor}\nAmbiente: {self.ambiente}\nVelocidade: {self.velocidade}')
