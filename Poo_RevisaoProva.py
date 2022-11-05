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

from datetime import date

#essa classe tá lindona
class Conta:
    def __init__(self, nm_cliente, n_conta, saldo):
        self._nm_cliente = nm_cliente
        self._n_conta = n_conta
        self._saldo = float(saldo)

    @property
    def nm_cliente(self):
        return self._nm_cliente
    
    @property
    def n_conta(self):
        return self._n_conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    def sacar(self, valor):
        #valor = float(input('Quanto quer sacar? '))
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo = self.saldo - valor
            print(f'\nAo sacar esse valor o saldo passa a ser R${self.saldo:.2f}'.format(self.saldo))
    
    def depositar(self):
        deposito = float(input('Quanto quer depositar? '))
        self.saldo = self.saldo + deposito
        print(f'\nO saldo na conta atualizado com o depósito é R${self.saldo:.2f}\n'.format(self.saldo))
    
    def imprimir(self):
        print(f'\nTitular da Conta --> {self.nm_cliente}')
        print(f'\nNúmero da Conta --> {self.n_conta}')
        print(f'\nSaldo na Conta --> R${self.saldo:.2f}'.format(self.saldo))



class ContaPoupanca(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, dt_rendimento):
        super().__init__(nm_cliente, n_conta, saldo)
        self.dt_rendimento = int(dt_rendimento)
        self.dt_hj = date.today().day
    
    def calcularNovoSaldo(self):
        if self.dt_hj == self.dt_rendimento:
            taxa = float(input('Valor da sua taxa de rendimento: '))
            rendimento = self.saldo * (taxa / 100)
            self.saldo = self.saldo + rendimento
            print(f'\nAtualizamos sua conta com sua taxa de rendimento e seu saldo passou a ser R${self.saldo:.2f}'.format(self.saldo))
        else:
            print(f'\nO dia do seu rendimento é {self.dt_rendimento}, tente novamente em {self.dt_rendimento - self.dt_hj} dias')
    
    def depositar(self):
        deposito = float(input('\nQuanto quer depositar? \n'))
        self.saldo = self.saldo + deposito
        print(f'\nO saldo na conta atualizado com o depósito é R${self.saldo:.2f}'.format(self.saldo))
    
    def imprimir(self):
        print(f'Data do rendimento da Conta --> {self.dt_rendimento}')
        return super().imprimir()


#essa é a problemática
class ContaEspecial(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, limite):
        super().__init__(nm_cliente, n_conta, saldo)
        self.limite = float(limite)
    
    def sacarEspecial(self, valor):
        #valor = float(input('\nQuanto quer sacar? '))
        if self.saldo >= 0:
            if valor <= self.saldo + self.limite:
                if self.saldo >= valor:
                    self.sacar(valor)
                else:
                    self.saldo = self.saldo - valor
                    self.limite = self.limite - valor
                    #print(f'Seu saldo atual é R${self.saldo:.2f}, e seu limite {self.limite}'.format(self.saldo))
            else:
                print('Limite insuficiente')
        else:
            if self.limite - valor < 0:
                print('Limite insuficiente')
            else:
                self.saldo = self.saldo - valor
                self.limite = self.limite - valor
                #print(f'\nAo sacar esse valor o saldo passa a ser R${self.saldo:.2f}'.format(self.saldo))
    
    def depositar(self):
        deposito = float(input('\nQuanto quer depositar? '))
        self.saldo = self.saldo + deposito
        #self.limite = self.limite
        print(f'\nO saldo na conta atualizado com o depósito é R${self.saldo:.2f}\n'.format(self.saldo))
    
    def imprimir(self):
        print(f'Limite da Conta --> {self.limite}')
        return super().imprimir()


'''c = Conta('Alice', 209, 100.00)
c.depositar()
c.sacar()
c.imprimir()'''

'''cp = ContaPoupanca('Rui', 708, 55.40, 7)
cp.calcularNovoSaldo()
cp.depositar()
cp.imprimir()'''

ce = ContaEspecial('Maria', 465, 30, 60)
ce.sacarEspecial(40)
ce.imprimir()
