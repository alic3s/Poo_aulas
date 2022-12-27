from pagavel import Pagavel
from datetime import date

class Conta:
    def __init__(self, dia, mes, valor):
        self.dia = int(dia)
        self.mes = int(mes)
        self.valor = valor


class Titulo(Conta):
    def __init__(self, dia, mes, valor):
        super().__init__(dia, mes, valor)
    
    def getValorAPagar(self):
        if (self.dia > date.day) and (self.mes >= date.month):
            multa = self.valor + (self.valor * 0.1)
            print('O valor agora é: ', multa)

class Concessionária(Conta):
    def __init__(self, dia, mes, valor):
        super().__init__(dia, mes, valor)
    
    def getValorAPagar(self):
        self.valor = int(input('Informe o valor da conta a ser paga: '))
        
