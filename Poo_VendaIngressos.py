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

from datetime import date, datetime

class Ingresso:
    def __init__(self, valor = 200.00) -> None:
        self.valor = valor
        self.status = ''
        self.codigo = 0
    
    def __str__(self) -> str:
        return f'O valor do ingresso é {self.valor} e o status é {self.status} e o código único é {self.codigo}'

class Camarote(Ingresso):
    def __init__(self, valor=200, adicional=100):
        super().__init__(valor)
        self.adicional = valor + adicional
    
    def __str__(self) -> str:
        return f'O valor do ingresso é {self.adicional} e o status é {self.status} e o código único é {self.codigo}'

class Show:
    def __init__(self, artista, data, local) -> None:
        self.artista = artista
        self.data = datetime.date(data)
        self.local = local
        self.ipista = []
        self.icamarote = []
    
    def __str__(self) -> str:
        return f'O artista convidado é {self.artista}, no dia {self.data} no {self.local}'
    
    def gerarIngressos(self, quantidade, valor1, tipo):
        if tipo == 1:
            self.icamarote.append(quantidade)
        elif tipo == " ":
            self.ipista.append(quantidade)











i = Camarote()
i.status = 'aoba'
i.codigo = 34
print(i)
