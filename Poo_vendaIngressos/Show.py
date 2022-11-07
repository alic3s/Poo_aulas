from ingresso import Ingresso, Camarote

class Show:
    def __init__(self, artista, data, local) -> None:
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
    def ingressos(self):
        return self._ingressos
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
        return f'\n###### Informações do Show ######\nArtista convidado: {self._artista}\nData: {self._data}\nLocal: {self._local}'

    def gerarIngressos(self, quantidade, valor, tipo = None):
        if (tipo == None):
            for i in range(quantidade):
                ingresso = Ingresso(valor)
                self.ingressos = ingresso

        elif (tipo == 1):
            for i in range(quantidade):
                adicional = float(input('\nValor adicional do ingresso VIP: '))
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


    def relatorioVendas(self):
        print(self)
        total = 0
        
        print('\n' + '=' * 10 + 'Pista' + '=' * 10 + '\n')

        for i in self.ingressos:
            if i.status == 'Vendido':
                print(i, '\n')
                total += i.valor

        print('=' * 10 + 'Camarote' + '=' * 10 + '\n')

        for i in self.camarote:
            if i.status == 'Vendido':
                print(i, '\n')
                total += i.valor + i.adicional

        print(f'TOTAL = R${total:.2f}\n')
    
    def __str__(self) -> str:
        return f'\n###### Informações do Show ######\nArtista convidado: {self._artista}\nData: {self._data}\nLocal: {self._local}'





show1=Show('Lorde', '06/11/2022','Primavera Sound - SP')
print(show1)

show1.gerarIngressos(1,100) #ingresso pista
show1.gerarIngressos(1,200,1) #ingresso camarote/VIP


print(f'\nValor a pagar por 1 ingresso de pista: R${show1.venderIngresso(1)}') #um ingresso pista

print(f'Valor a pagar por 1 ingresso VIP: R${show1.venderIngresso(1,1)}\n') #um ingresso VIP

show1.relatorioVendas()
