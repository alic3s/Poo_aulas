'''Implemente as classes: Ingressos, Camarote, Show.

A classe Ingresso é composta por um código único, que deve ser gerado por um
método estático definido por você ao instanciar o objeto, um valor e um status, que
definirá se o ingresso já foi vendido. O construtor da classe deve receber como
parâmetro apenas o valor do ingresso. Sobrescreva o método __str__ para que faça a
impressão dos atributos da classe (código, status e valor). (1,0 ponto)

A classe Camarote é subclasse de Ingresso e possui como atributo específico um valor
adicional em relação ao ingresso de pista. Este valor adicional deve ser passado como
parâmetro no construtor da classe. Sobrescreva o método __str__ para que faça a
impressão dos atributos da classe (código, status e valor), atenção ao valor do ingresso
de camarote que deve ser mostrado já com a soma do adicional.(1,0 ponto)

A classe Show que possui como atributos: nome do Artista, Data do show, local do show
e duas listas: uma dos ingressos de pista e outra dos ingressos Camarote que devem
ser inicializadas vazias.(0,5 ponto) Defina um construtor que receba as informações do
artista, data e local. Esta classe possui quatro métodos, fora o construtor:
__str__(), que deve imprimir as informações do Show: artista, data e local. (0,5
ponto)

gerarIngressos( quantidade, valor, tipo), sendo o tipo opcional. Neste caso, ao
invocar o método sem o tipo, serão gerados uma certa quantidade de ingressos da pista
com o valor passado por argumento. Caso o tipo seja 1, os ingressos gerados devem
ser para o camarote, neste caso deve ser solicitado o valor adicional em relação ao
ingresso de pista.(1,0 ponto)

venderIngresso(quantidade, tipo), sendo o tipo opcional. Neste caso, ao
invocar o método sem o tipo, estaremos vendendo ingressos da pista. No caso de
passar o tipo 1, estaremos vendendo ingressos do camarote. Em ambos os casos,o
método deve alterar o status do ingresso para 'Vendido' e retornar o valor total da
compra.(1,0 ponto)

relatorioVendas(), neste método deverá ser apresentado a lista de todos os
ingressos vendidos até o presente momento, apresentando as informações do ingresso,
e apresentando ao final o total arrecadado com a venda dos ingressos(pista e
camarote). No cabeçalho do relatório deve aparecer os dados do show.(1,0 ponto)'''

from datetime import date

class Ingresso:
    aux = 0
    def __init__(self, valor):
        self._cod =__class__.gerarCodigo()
        self._valor = float(valor)
        self.status = None
    
    @property
    def cod(self):
        return self._cod
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    
    def __str__(self):
        return f"Código: {self.cod}\nValor: {self.valor}\nStatus: {self.status}"
    
    @staticmethod
    def gerarCodigo():
        ano = str(date.today())
        Ingresso.aux = Ingresso.aux + 1
        return ano + str(Ingresso.aux)



class Camarote(Ingresso):
    def __init__(self, valor, adicional):
        Ingresso.__init__(self, valor)
        self._adicional = float(adicional)
    
    @property
    def adicional(self):
        return self._adicional
    
    #@adicional.setter
    #def adicional(self, adicional):
        #self._adicional = adicional
    
    def __str__(self):
        return f"Código: {self.cod}\nValor: {self.valor + self.adicional}\nStatus: {self.status}"
