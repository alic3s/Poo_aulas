class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
class Ingles(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)
    
    def saudacao(self):
        print(f'Hi {self.nome}!')

class Portugues(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)
    
    def saudacao(self):
        print(f'Olá, {self.nome}!')
    
class Poliglota(Portugues, Ingles):
    def __init__(self, nome):
        Ingles.__init__(self, nome)
        Portugues.__init__(self, nome)


teste = Poliglota('Poliglota')

teste.saudacao()

print(Poliglota.mro())
