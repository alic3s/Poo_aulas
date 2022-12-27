from salario import ControlePagamento

class Empregado:
    def __init__(self, nome, sobrenome, numident):
        self.nome = str(nome)
        self.sobrenome = str(sobrenome)
        self.numident = numident
    

class Assalariado(Empregado):
    def __init__(self, nome, sobrenome, numident):
        super().__init__(nome, sobrenome, numident)
