class Agenda:
    def __init__(self):
        self.contatos = []

    def pesquisar_nome(self, nome):
        self.contato = contato
        
    def alterar_contato(self, nome):
        self.contato = ''
        
    def add_contato(self, contato):
        self.contatos.append(contato)
        
        
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
    
    def str(self):
    f'Esse é o nome: {self.nome.str}'
    f'Esse é o telefone: {self.telefone.str}'
    f'Esse é o email: {self.email.str}'


class Telefone:
    def __init__(self, DDD, numero, descricao):
        self.DDD = DDD
        self.numero = numero
        self.descricao = descricao
    
    def alterar_numero(self, numero):
        self.numero = numero


print('-' * 25 + '\n' + 'AGENDA'.center(25) + '\n' + '-' * 25)

dicio = {'1)': 'Inserir Contato', '2)': 'Pesquisar Contatos', '3)': 'Alterar Contatos', '4)': 'Sair'}

for k, v in dicio.items():
    print(f'{(k)} {v:^5}')

  
print ("""
    1.Inserir Contato
    2.Pesquisar Contato
    3.Alterar Contato
    4.Sair
    """)

menu = True
while menu:
    menu = int(input('Escolha uma opção: '))
if menu == 1:
    contato1 = Contato()
    agenda.add.contato
elif menu == 2:
    agenda.pesquisar_nome
    print(nome.self.contato)
elif menu == 3:
    print ("""
    3.1.Nome
    3.2.Email
    3.3.Telefone
    """)
    alterar = (float(input('Qual informação deseja alterar?: ')))
    if alterar == 3.1:
        contato.alterar_nome
        print(self.nome)
    elif alterar == 3.2:
        contato.alterar_email
        print(self.email)
    elif alterar == 3.3:
        contato.alterar_telefone
        print(self.telefone)
elif menu == 4:
    break
