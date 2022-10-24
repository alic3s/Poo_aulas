from ingresso import Ingresso, Camarote

class Show:
    def __init__(self, artista, data, local) -> None:
        aux = 0
        aux2 = 0
        self.artista = artista
        self.data = data
        self.local = local
        self._pista = list()
        self._camarote = list()
    
    @property
    def pista(self):
        return self._pista
    
    @pista.setter
    def pista(self, valor):
        self.pista.append(valor)
    
    @property
    def camarote(self):
        return self._camarote
    
    @camarote.setter
    def camarote(self, valor2):
        self.camarote.append(valor2)

    def __str__(self) -> str:
        return f'###### Informações do Show ######\nArtista convidado: {self.artista}\nData: {self.data}\nLocal: {self.local}'

    def gerarIngressos(self, quantidade, valor, tipo = None):
        if tipo == None:
            for i in range(quantidade):
                novo_ingresso = Ingresso(valor)
                self.pista(quantidade, novo_ingresso)
        elif tipo == 1:
            adicional = float(input('Valor adicional: '))
            valor2 = valor + adicional
            for i in range(quantidade):
                novo_ingresso = Camarote(valor2)
                self.camarote(quantidade, novo_ingresso)

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
