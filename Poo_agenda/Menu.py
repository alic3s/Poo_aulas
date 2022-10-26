from Contato import Telefone, Contato, Agenda

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
        contato1 = Contato(str(input('Nome do Contato: ')), input('Email do Contato: '), int(input('Telefone do Contato: ')))
        Agenda.add_contato((contato1))
    elif menu == 2:
        Agenda.pesquisar_nome()
    if menu == 3:
        print ("""
        3.1.Nome
        3.2.Email
        3.3.Telefone
        """)
    alterar = Contato(float(input('Qual informação deseja alterar?: ')))
    if alterar == 3.1:
        Contato.alterar_nome
    if alterar == 3.2:
        Contato.alterar_email
    if alterar == 3.3:
        Contato.alterar_telefone
    else:
        break


'''print('-' * 25 + '\n' + 'AGENDA'.center(25) + '\n' + '-' * 25)

dicio = {'1)': 'Inserir Contato', '2)': 'Pesquisar Contatos', '3)': 'Alterar Contatos', '4)': 'Sair'}

for k, v in dicio.items():
    print(f'{(k)} {v:^5}')
    
    
from Contato import Contato, Telefone, Agenda

t1 = Telefone(79, 998515346, 'Casa')
t2 = Telefone(79, 998904776, 'Apê')

Alice = Contato('Alice', 'asa1234@hotmmail.com', t1)
Alice.alterar_nome('Alici')

aA = Agenda(Alice)
print(aA.pesquisar_nome('Alici'))
aA.add_contato(Alice)

print(Alice)
