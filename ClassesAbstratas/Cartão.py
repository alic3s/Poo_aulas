from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, sobrenome, email) -> str:
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

        
class Remetente(Pessoa):
    def __init__(self, nome, sobrenome, email) -> str:
        super().__init__(nome, sobrenome, email)
        self._lista = []
    
    @property
    def lista(self):
        return self._lista
    @lista.setter
    def lista(self):
        self._lista = []
        

    def addCartao(self, cartao):
        self.lista.append(cartao)
    
    def showCartao(self, cartao):
        if cartao == Diadosnamorados:
            print(f'Nome do destinatário: {Cartao.destinatario.nome} {Cartao.destinatario.sobrenome}\nMensagem do cartão: {Diadosnamorados}\nMensagem particular: {cartao.messagePlus}\nAss: {self.nome} {self.sobrenome}')
        if cartao == Natal:
            print(f'Nome do destinatário: {Cartao.destinatario.nome} {Cartao.destinatario.sobrenome}\nMensagem do cartão: {Natal}\nMensagem particular: {cartao.messagePlus}\nAss: {self.nome} {self.sobrenome}')
        if cartao == Aniversario:
            print(f'Nome do destinatário: {Cartao.destinatario.nome} {Cartao.destinatario.sobrenome}\nMensagem do cartão: {Aniversario}\nMensagem particular: {cartao.messagePlus}\nAss: {self.nome} {self.sobrenome}')
    

class Cartao(ABC):
    def __init__(self, destinatario: Pessoa, messagePlus: str = None):
        self.destinatario = destinatario
        self.messagePlus = messagePlus

    @abstractmethod
    def showMessage(self):
        pass


class Diadosnamorados(Cartao):
    def showMessage():
        print('Feliz Dia dos Namorados!')

class Natal(Cartao):
    def showMessage():
        print('Feliz Natal!')

class Aniversario(Cartao):
    def showMessage():
        print('Feliz Aniversário!')
    

remetente=Remetente('Cris','Oliveira','cris@gmail.com')
destinatario=Pessoa('Maria','Oliveira','maria@gmail.com')
cartao2=Natal(destinatario)
remetente.addCartao(cartao2)
remetente.showCartao(cartao2)
