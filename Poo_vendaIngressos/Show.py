class Show:
    def __init__(self, artista, data, local) -> None:
        #aux = 0
        #aux2 = 0
        self._artista = artista
        self._data = data
        self._local = local
        self._ingressos = []
        self._camarote = []
    
    @property
    def artista(self):
        return self._artista
    
    @property
    def data(self):
        return self._data

    @property
    def local(self):
        return self._local
    
    @property
    def pista(self):
        return self._pista
    @ingressos.setter
    def ingressos(self, ingresso):
        self._ingressos.append(ingresso)
    
    @property
    def camarote(self):
        return self._camarote
    @camarote.setter
    def camarote(self, camarote):
        self.camarote.append(camarote)

    def __str__(self) -> str:
        return f'###### Informações do Show ######\nArtista convidado: {self._artista}\nData: {self._data}\nLocal: {self._local}'

    def gerarIngressos(self, quantidade, valor, tipo = None):
        if (tipo == None):
            for i in range(quantidade):
                ingresso = Ingresso(valor)
                self.ingressos = ingresso

        elif (tipo == 1):
            adicional = float(input('Valor adicional: '))
            for i in range(quantidade):
                ingresso = Camarote(valor, adicional)
                self.camarote = ingresso
        
        else:
            print('Tipo inválido')

    def venderIngresso(self, quantidade, tipo = None):
        total = 0
        cont = 0
        if (tipo == None):
            for elemento in self.ingressos:
                if (elemento.status == None) and (cont != quantidade):
                    elemento.status = 'Vendido'
                    total += elemento.valor
                    cont += 1

        elif(tipo == 1):
            for elemento in self.camarote:
                if (elemento.status == None) and (cont != quantidade):
                    elemento.status = 'Vendido'
                    total += (elemento.valor + elemento.adicional)
                    cont += 1
        return total

    def relatorioPista(self):
        print(self)
        total = 0
        for elemento in self.ingressos:
            if elemento in self.ingressos:
                if elemento.status == 'Vendido':
                    print(elemento)
                    total += elemento.valor

            for elemento in self.camarote:
                if elemento.status == 'Vendido':
                    print(elemento)
                    total += elemento.valor + elemento.adicional
