from Contato import Telefone, Contato, Agenda

print('-' * 25 + '\n' + 'AGENDA'.center(24) + '\n' + '-' * 25)

print ("""
    1.Inserir Contato
    2.Pesquisar Contato
    3.Alterar Contato
    4.Sair
    """)

while True:
    menu = int(input('Escolha uma opção: '))

    if menu == 1:
        contato = Contato(str(input('Nome do Contato: ')), input('Email do Contato: '), int(input('Telefone do Contato: ')))
        Agenda.add_contato()

    elif menu == 2:
        Agenda.pesquisar_nome(Agenda, nome=Contato)

    elif menu == 3:
        print ("""
            3.1.Nome
            3.2.Email
            3.3.Telefone
            """)

        alterar = (float(input('Qual informação deseja alterar?: ')))

        if alterar == 3.1:
            Contato.alterar_nome()

        elif alterar == 3.2:
            Contato.alterar_email()

        elif alterar == 3.3:
            Contato.alterar_telefone()
            
    else:
        print('Opção inválida!')
        break
