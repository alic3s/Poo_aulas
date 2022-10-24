class Telefone:
    def __init__(self, ddd, numero, descricao):
        self.ddd = ddd
        self.numero = numero
        self.descricao = descricao
    
    def alterar_numero(self, numero):
        self.numero = numero

    def __str__(self):
        return '({0}) {1} --> {2}'.format(self.ddd, self.numero, self.descricao)


class Contato:
    def __init__(self, nome, email, telefone: Telefone):
        self.nome = nome
        self.email = email
        self.telefone = [telefone]
    
    def alterar_email(self, email):
        self.email = email
    
    def alterar_telefone(self, telefone: Telefone):
        if len(self.telefone) <= 3:
            self.telefone.append(telefone)
        else:
            print('Memória cheia')
    
    def alterar_nome(self, nome):
        self.nome = nome
    
    def __str__(self):
        texto = f'Nome: {self.nome}\nEmail: {self.email}\nTelefones:{self.telefone}\n'
        for item in self.telefone:
            if item != None:
                texto += str(item) + " "
        return texto


class Agenda:
    def __init__(self, contatos: Contato):
        self.contatos = [contatos]

    def pesquisar_nome(self, nome) -> Contato:
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None
        
    def alterar_contato(self, nm_antigo, nm_novo, email, telefone: Telefone):
        antigo = self.pesquisar_nome(nm_antigo)
        novo = Contato(nm_novo, email, telefone)
        self.contatos[self.contatos.index(antigo)] = novo
        
    def add_contato(self, contato: Contato):
        if len(self.contatos) <= 10:
            self.contatos.append(contato)
        else:
            print('Agenda cheia!')
