from galeria import Artistas, Galeria, Obra, Pintura, Escultura

def principal():
    print('''
    1. Adicionar uma unidade à rede de galerias
    2. Realizar ações numa galeria específica #nesse caso você deve solicitar ao usuário
qual o nome da unidade)
    ''')
principal()

opc = int(input('Escolha uma opção: '))

if opc == 1:
