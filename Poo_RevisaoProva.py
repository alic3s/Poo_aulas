'''Elabore uma classe Conta, com os seguintes atributos: nome_cliente, num_conta,
saldo e os métodos: sacar(valor) e depositar(valor).
Não permita realizar saque de forma que o saldo fique negativo.
Acrescente ao projeto a classe ContaPoupanca e ContaEspecial que são subclasses
da classe Conta.
Classe ContaPoupanca: com atributo dia_rendimento (inteiro) e um método:
calcularNovoSaldo que recebe a taxa de rendimento e atualiza o saldo.
Classe ContaEspecial: com atributo limite e um método sacar permitindo o saldo
negativo até o valor do limite.
No programa principal implemente:
Instanciar objetos referentes às contas.
Sacar valor das contas
Depositar valor nas contas
Mostrar novo saldo, a partir da taxa de rendimento, da conta poupança.
Mostrar os dados da conta de um cliente.'''

class Conta:
    def __init__(self, nm_cliente, n_conta, saldo):
        self.nm_cliente = nm_cliente
        self.n_conta = n_conta
        self.saldo = saldo
    
    def sacar(self):
        valor = float(input('Valor a ser sacado: '))
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            print(f'O saldo atual é {self.saldo - valor}')
    
    def depositar(self):
        deposito = float(input('Valor a ser depositado: '))
        print(f'O saldo na conta atualizado com o depósito é: {self.saldo + deposito}')

class ContaPoupanca(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, dia_rendimento):
        super().__init__(nm_cliente, n_conta, saldo)
        self.dia_rendimento = int(dia_rendimento)
    
    def calcularNovoSaldo(self):


class ContaEspecial(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, limite):
        super().__init__(nm_cliente, n_conta, saldo)
        self.limite = float(limite)
    
    def sacar(self):
        

c = Conta('Alice', 123, 45.00)

c.depositar()
c.sacar()
