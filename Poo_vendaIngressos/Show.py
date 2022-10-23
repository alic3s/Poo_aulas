from ingresso import Ingresso, Camarote

class Show:
    def __init__(self, artista, data, local) -> None:
        aux = 0
        aux2 = 0
        self.artista = artista
        self.data = data
        self.local = local
        self.pista = []
        self.camarote = []
    
    def __str__(self) -> str:
        return f'###### Informações do Show ######\nArtista convidado: {self.artista}\nData: {self.data}\nLocal: {self.local}'

    def gerarIngressos(self, quantidade, valor, tipo = None):
        if tipo == None:
            for i in range(quantidade):
                self.ingresso.append(Ingresso(valor))
        else:
            adicional = float(input('Valor adicional: '))
            for i in range(quantidade):
                self.camarote.append(Camarote(valor, adicional))

    def venderIngresso(self, quantidade, tipo = None):
        if tipo == None:
            for i in range(quantidade):
                self.ingresso[Show.aux].vender()
                Show.aux += 1
        else:
            for i in range(quantidade):
                self.camarote[Show.aux2].vender()
                Show.aux2 += 1

    def relatorioPista(self):
        for i in range(len(self.ingresso)):
            print(self.ingresso[i])
    
    def relatorioCamarote(self):
        for i in range(len(self.camarote[i])):
            print(self.camarote[i])
