class Contato:
    def __init__(self, nome, email = None):
        self.nome = nome
        self.email = email
        self.telefone = []
    
    def alterar_email(self, email):
        self.email = email
    
    def alterar_telefone(self, telefone):
        self.telefone = telefone
    
    def alterar_nome(self, nome):
        self.nome = nome
    
    def imprimir(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)


class Telefone:
    def __init__(self, DDD, numero, descricao):
        self.DDD = DDD
        self.numero = numero
        self.descricao = descricao
    
    def alterar_numero(self, numero):
        self.numero = numero

class Agenda:
    def __init__(self):
        self.contatos = []

    def pesquisar_nome(self, nome):
        self.contatos



print('-' * 25 + '\n' + 'AGENDA'.center(25) + '\n' + '-' * 25)

dicio = {'1)': 'Inserir Contato', '2)': 'Pesquisar Contatos', '3)': 'Alterar Contatos', '4)': 'Sair'}

for k, v in dicio.items():
    print(f'{(k)} {v:^5}')
