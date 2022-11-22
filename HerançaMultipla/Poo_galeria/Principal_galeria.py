from galeria import Artistas, Galeria, Obra, Pintura, Escultura

def principal():
    print('''
    1. Adicionar uma unidade à rede de galerias
    2. Realizar ações numa galeria específica
    ''')
principal()

opc = int(input('Escolha uma opção: '))

if opc == 2:
    nova_galeria = Galeria(input('Informe o nome da unidade: '), int(input('Informe o telefone local: ')), input('Informe o nome do responsável pela unidade: '))
    Unidade1 = nova_galeria
    #(pintura e escultura) (imprimir em tela: código, título, autor de cada obra, técnica, tipo de tinta(para pintura) e tipo de material(para escultura))
    print('''
    2.1 – Cadastrar uma Obra
    2.2 – Listar Obras da galeria
    2.3 – Listar Obras de um determinado Artista(nome).
    2.4 – Permitir avaliar uma obra, a partir do seu código
    2.5 - Finalizar atividades nesta galeria
    3. Finalizar Sistema
    ''')
    sub = float(input('Escolha uma opção: '))

    if sub == 2.1:
        nova_obra = Obra(input('Data de aquisição: '), input('Título: '), input('Técnica: '), float(input('Valor: ')), input('Autor: '))
        #como pedir o codigo?
        nova_obra.imprimirObra()
