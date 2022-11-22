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

print('#' * 25 + 'CONTA BANCÁRIA'.center(20) + '#' * 25)

#essa classe tá lindona
class Conta:
    def __init__(self, nm_cliente, n_conta, saldo):
        self._nm_cliente = nm_cliente
        self._n_conta = n_conta
        self._saldo = float(saldo)

    #nao faz alteração nesses atributos
    @property
    def nm_cliente(self):
        return self._nm_cliente
    
    @property
    def n_conta(self):
        return self._n_conta
    
    @property
    def saldo(self):
        return self._saldo
    
    #o método sacar faz a alteração no saldo, ou seja, não precisa do setter
    #@saldo.setter
    #def saldo(self, saldo):
    #    self._saldo = saldo
    
    def sacar(self):
        valor = float(input('\nQuanto quer sacar? '))
        if valor > self.saldo:
            print(f'\nSaldo insuficiente. Saldo R${self.saldo:.2f}'.format(self.saldo))
        else:
            self._saldo -= valor
            print(f'\nAo sacar esse valor o saldo passa a ser R${self.saldo:.2f}'.format(self.saldo))
    
    def depositar(self):
        valor = float(input('\nQuanto quer depositar? '))
        self._saldo += valor
        print(f'O saldo na conta atualizado com o depósito é R${self.saldo:.2f}\n'.format(self.saldo))
    
    def imprimir(self):
        #podia ser --> def __str__(self):
        #               return f'Titular: {self._nm_cliente}\n Conta....
        print(f'\nTitular da Conta --> {self._nm_cliente}')
        print(f'\nNúmero da Conta --> {self._n_conta}')
        print(f'\nSaldo na Conta --> R${self._saldo:.2f}'.format(self._saldo))



class ContaPoupanca(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, dt_rendimento):
        super().__init__(nm_cliente, n_conta, saldo)
        self._dt_rendimento = int(dt_rendimento)
        self.dt_hj = date.today().day
    
    @property
    def dt_rendimento(self):
        return self._dt_rendimento

    def calcularNovoSaldo(self):
        if self.dt_hj == self.dt_rendimento:
            taxa = float(input('\nValor da sua taxa de rendimento: '))
            rendimento = self.saldo * (taxa / 100)
            self._saldo += rendimento
            print(f'Rendimento R${rendimento:.2f}'.format(rendimento))
            print(f'Saldo atual R${self.saldo:.2f}'.format(self.saldo))
        else:
            print(f'\nO dia do seu rendimento é {self.dt_rendimento}, tente novamente em {self.dt_rendimento - self.dt_hj} dias')
    
    #esse método é igual o da classe pai, ou seja, não precisa fazer de novo
    #def depositar(self):
        #deposito = float(input('\nQuanto quer depositar? \n'))
        #self.saldo = self.saldo + deposito
        #print(f'\nO saldo na conta atualizado com o depósito é R${self.saldo:.2f}'.format(self.saldo))
    
    def imprimir(self):
        print(f'\nData do rendimento da Conta --> {self.dt_rendimento}')
        return super().imprimir()


#essa é a problemática e eu ainda não entendo ela
class ContaEspecial(Conta):
    def __init__(self, nm_cliente, n_conta, saldo, limite):
        super().__init__(nm_cliente, n_conta, saldo)
        self._limite = float(limite)
        self._limite1 = self._limite
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def limite1(self):
        return self._limite1
    
    #podia ter um setter, mas não que fosse necessário
    
    def sacar(self):
        valor = float(input('\nQuanto quer sacar? '))
        if valor > self.saldo + self.limite:
            print(f'Saldo insuficiente. \nSaldo R${self.saldo:.2f}'.format(self.saldo))
        else:
            if valor < self.saldo:
                self._saldo -= valor
                print(f'Saldo atual R${self.saldo:.2f}\nLimite atual R${self.limite:.2f}'.format(self.saldo, self.limite))
                print(f'Saldo disponível com limite R$ {self.saldo + self.limite}')
            else:
                self._saldo -= valor
                self._limite += self.saldo
                print(f'Saldo atual R${self.saldo:.2f}\nLimite atual R${self.limite:.2f}'.format(self.saldo, self.limite))
                
                if self.saldo > self.limite:
                    print(f'Saldo real R${self.saldo}')
                else:
                    print('Saldo real R$%.2f'%(self.saldo))
                    print(f'Saldo disponível com limite R$ {self.saldo + self.limite}')
    
    #esse método também é igual ao da conta pai, não precisava repetir
    #def depositar(self):
        #deposito = float(input('\nQuanto quer depositar? '))
        #self.saldo = self.saldo + deposito
        #self.limite = self.limite
        #print(f'\nO saldo na conta atualizado com o depósito é R${self.saldo:.2f}\n'.format(self.saldo))
    
    def imprimir(self):
        print(f'\nLimite da Conta --> {self.limite1}')
        return super().imprimir()


'''c = Conta('Alice', 209, 100.00)
c.depositar()
c.sacar()
c.imprimir()'''

'''cp = ContaPoupanca('Rui', 708, 55.40, 7)
cp.calcularNovoSaldo()
cp.depositar()
cp.imprimir()'''

ce = ContaEspecial('Maria', 465, 1000, 1000)
ce.depositar()
ce.sacar()
ce.imprimir()
