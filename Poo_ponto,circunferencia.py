class Ponto:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
    
    def alterar_cor(self, nova_cor = ''):
       self.cor = nova_cor

    def imprimir(self):
        print(f'O valor do ponto X é: {self.x}')
        print(f'O valor do ponto Y é: {self.y}')
        print(f'A nova cor é: {self.cor}')

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

    def imprimir_2(self):
        print(f'O centro da circunferência é {self.centro}')
        print(f'O raio da circunferência é {self.raio}')
        print(f'A cor da linha da circunferência é {self.cor_linha}')
        print(f'A cor do preenchimento da circunferência é {self.cor_preenchimento}')
