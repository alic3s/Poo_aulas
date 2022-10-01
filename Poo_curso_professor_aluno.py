class Curso:
    def __init__(self, codigo, nome, descricao, coordenador):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.coordenador = coordenador
        self.docentes = []
        
    def definir_coordenador(self, professor):
        self.coordenador = professor
    
    def add_docente(self, professor):
        self.docentes.append(professor)

    def __str__ (self):
        return f"[O código do curso é: {self.codigo}, o nome é: {self.nome}, sua descrição: {self.descricao}, o coordenador: {self.coordenador} e os docentes: {self.docentes}]"

class Professor:
    def __init__(self, matricula, nome_, cpf, admissao, email):
        self.matricula = matricula
        self.nome_ = nome_
        self.cpf = cpf
        self.admissao = admissao
        self.email = email
        self.lotacao = None
    
    def set_lotacao(self, curso: Curso):
        self.lotacao = curso

    def __str__ (self):
        return f' [Matrícula: {self.matricula}, o nome: {self.nome_}, cpf: {self.cpf}, admissao: {self.admissao} email: {self.email}, lotação: {self.lotacao}]'

class Aluno:
    def __init__(self, matricula_a, nome_a, cpf_a, email_a = None):
        self.matricula_a = matricula_a
        self.nome_a = nome_a
        self.cpf_a = cpf_a
        self.email_a = email_a
        self.cursos = []
    
    def matricular(self, curso):
        self.cursos.append(curso)
        print(f'Estes são os cursos no qual o aluno está matriculado: {self.cursos}')
    
    def imprimir(self):
        print(f'A matricula do aluno é: {self.matricula_a}')
        print(f'O nome do aluno é: {self.nome_a}')
        print(f'O cpf do aluno é: {self.cpf_a}')
        print(f'O email do aluno: {self.email_a}')
        print(f'Os cursos que o aluno faz são: {self.cursos}')

biologia = Curso(123, 'Biologia', 'Dificil', 'Jorginho')
carlos = Professor(123132, 'Carlos', 123123123, '123d1s2a3ds', '213123')
pedro = Professor(12345, 'Pedro', 56576, '6yhg277', '65579')
biologia.add_docente(carlos)
biologia.add_docente(pedro)

print(biologia)
