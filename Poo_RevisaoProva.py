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
        self.saldo = self.saldo + deposito
        print(f'O saldo na conta atualizado com o depósito é: {self.saldo}')

class ContaPoupanca(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, dia_rendimento):
        super().__init__(nm_cliente, n_conta, saldo)
        self.dia_rendimento = int(dia_rendimento)
    
    def calcularNovoSaldo(self):
        #nao sei como verificar se é ou não a data de aniversário do depósito
        '''O rendimento, como já explicado, é de 0,5% por cento ao mês com a Taxa Selic em vigor. O rendimento é creditado em sua conta mensalmente,
        no dia do aniversário do depósito. Por exemplo, se você fez um depósito de R$100,00 no dia 15 de algum mês,
        os juros vão cair no dia 15 do mês seguinte.'''
        #self.saldo = self.saldo * 0,5

class ContaEspecial(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, limite):
        super().__init__(nm_cliente, n_conta, saldo)
        self.limite = float(limite)
    
    def sacar(self):
        #to no caminho mas com certeza ta errado
        sacar = float(input('Valor a ser sacado: '))
        if sacar > self.limite:
            self.saldo = -self.limite
            print('Seu saldo atual é {}', self.saldo, 'e ao sacar passa a ser {}', (self.saldo - sacar))
        else:
            print(f'Seu saldo ao sacar é {self.saldo - sacar}')

c = ContaEspecial('Alice', 123, 200.00, 400.00)

c.sacar()
