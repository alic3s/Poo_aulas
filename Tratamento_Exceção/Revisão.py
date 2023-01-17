from abc import ABC, abstractmethod
class iAutenticavel(ABC):
    @abstractmethod
    def autenticar(self):
        pass

class SaldoExcecaoError(Exception):
    pass

def validarSaque(self, saque):
    if saque > self.saldo:
        raise SaldoExcecaoError('Saque maior que o saldo.')

class Conta:
    def __init__(self, agencia=str, numConta=int, saldo=float, senha=str):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo
        self.senha = senha
    
    def depositar(self, valor) -> float:
        try:
            self.saldo += valor
        except TypeError:
            print('Erro: Tipo Inválido!')
       

    def sacar(self) -> float:
        try:
            s = input(float('Valor a ser sacado: '))
            validarSaque(s)
        except SaldoExcecaoError as e:
            print(f'ERRO {e}')
