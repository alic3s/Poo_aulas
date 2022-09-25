class Vaca:
    def __init__ (self, registro, peso, raca, cor):
        self.registro = registro
        self.raca = raca
        self.cor = cor
        self.tamanho = 0.0
        self.idade = 0
        self.peso = 0.0
        self.leite = 0.0

    def comer (self, alimento, quantidade):
        self.peso += quantidade*0.05
        print(f"A vaca comeu {quantidade} kg de {alimento}")
    
    def ruminar (self):
        print('Urrrrrrrgh...nhek, nhek, nhek.')
    
    def produzirLeite(self):
        self.leite = self.peso * 0.02
        print('A vaca produziu', str(leite), 'litros de leite')
        return self.leite
    
    def caminhar(self, distancia):
        print('Tek tek tek...uf, a vaca caminhou: ', distancia, 'metros')
    
    def imprimir(self):
        print(f'O registro da vaca é: {self.registro}')
        print(f'A raça da vaca é {self.raca}')
        print(f'A cor da vaca é {self.cor}')
        print(f'O tamanho dela é {self.tamanho}')
        print(f'A idade dela é {self.idade}')
        print(f'O peso dela é {self.peso}')
        

Mimosa = Vaca
Mimosa.registro = 12345
Mimosa.peso = 60
Mimosa.cor = 'Preto'
Mimosa.comer('grama', 10);

print(Mimosa.registro, Mimosa.peso, Mimosa.cor)
print(Mimosa.comer)
