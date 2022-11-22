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
    def __init__(self, nome, sobrenome, email, cartoes) -> str:
        super().__init__(nome, sobrenome, email)
        self._lista = []
        for c in cartoes:
            self._lista.append(c)
    
    @property
    def lista(self):
        return self._lista
        
    
    def addCartao(self, cartoes):
        self._lista.append(cartoes)
    
    def showCartao(self, cartoes):
        if cartoes == 1:
            f'Nome do destinatário: {self.destinatario.nome}, {self.destinatario.sobrenome}\nMensagem do cartão: \nMensagem particular: \nAss: '
    

class Cartao(ABC):
    def __init__(self, destinatario: Pessoa, messagePlus = None):
        self.destinatario = destinatario
        self.messagePlus = messagePlus((input('Informe a mensagem que deseja enviar --> ')))

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
