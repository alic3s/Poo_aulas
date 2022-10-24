'''print('-' * 25 + '\n' + 'AGENDA'.center(25) + '\n' + '-' * 25)

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
    break'''


from Contato import Contato, Telefone, Agenda

t1 = Telefone(79, 998515346, 'Casa')
t2 = Telefone(79, 998904776, 'Apê')

Alice = Contato('Alice', 'asa1234@hotmmail.com', t1)
Alice.alterar_nome('Alici')

aA = Agenda(Alice)
print(aA.pesquisar_nome('Alici'))
aA.add_contato(Alice)

print(Alice)
