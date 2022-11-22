from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, sobrenome, email) -> str:
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @property
    def email(self):
        return self._email


class Remetente(Pessoa):
    def __init__(self, nome, sobrenome, email) -> str:
        super().__init__(nome, sobrenome, email)
        self._lista = []
    
    @property
    def lista(self):
        return self._lista
        
    
    def addCartao(self, cartao):
        self._lista.append(cartao)
    
    def showCartao(self, cartao):
        if cartao == Diadosnamorados:
            return f'Nome do destinatário: {cartao.destinatario.nome} {cartao.destinatario.sobrenome}\nMensagem do cartão: {Diadosnamorados.showMessage}\nMensagem particular: {cartao.messagePlus}\nAss: {self.nome} {self.sobrenome}'
    

class Cartao(ABC):
    def __init__(self, destinatario: Pessoa, messagePlus = input('Mensagem particular: ')):
        self.destinatario = destinatario
        self.messagePlus = messagePlus

    @abstractmethod
    def showMessage(self):
        pass

class Diadosnamorados(Cartao):
    def showMessage(self):
        print('Feliz Dia dos Namorados!')

class Natal(Cartao):
    def showMessage(self):
        print('Feliz Natal!')

class Aniversario(Cartao):
    def showMessage(self):
        print('Feliz Aniversário!')
