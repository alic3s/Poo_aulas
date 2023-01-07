from salario import ControlePagamento

class Empregado(ControlePagamento):
    def __init__(self, salario=1100, hora=8, nome=str, sobrenome=str, numident=float):
        super().__init__(salario, hora)
        self.nome = nome
        self.sobrenome = sobrenome
        self.numident = numident
    

class Assalariado(Empregado):
    def __init__(self, salario=1100, hora=8, nome=str, sobrenome=str, numident=float, horasem=int, horaextra=None):
        super().__init__(salario, hora, nome, sobrenome, numident, horasem, horaextra)
        self.horasem = horasem
        self.horaextra = horaextra 

    def getValorAPagar(self):
        if self.horasem == 40:
            print('Salário fixo de ', self.salario)
        elif self.horasem > 40:
            print('Salário fixo acrescido das horas extras ', self.salario + (self.hora * self.horaextra))


class Terceirizado(Empregado):
    def __init__(self, salario=1100, hora=8, nome=str, sobrenome=str, numident=float, horasem=int):
        super().__init__(salario, hora, nome, sobrenome, numident, horasem)
        self.horasem = horasem

    def getValorAPagar(self):
        print('Salário por hora trabalhada ', self.horasem * self.hora)


class Comissionado(Empregado):
    def __init__(self, salario=1100, hora=8, nome=str, sobrenome=str, numident=float, vendas = float):
        super().__init__(salario, hora, nome, sobrenome, numident, vendas)
        self.vendas = vendas
    
    def getValorAPagar(self):
        print('Salário com porcentagem sobre as vendas ', self.vendas + (0.06 * self.vendas))


class AssalariadosComissionados(Comissionado):
    def __init__(self, salario=1100, hora=8, nome=str, sobrenome=str, numident=float, vendas=float):
        super().__init__(salario, hora, nome, sobrenome, numident, vendas)
        self.vendas = vendas
    
    def getValorAPagar(self):
        print('Salário ', (self.salario + (0.10 * self.salario)) + (self.salario + (0.06 * self.vendas)))
