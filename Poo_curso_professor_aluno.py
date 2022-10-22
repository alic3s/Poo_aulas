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
        return f"[Código: {self.codigo}\nNome: {self.nome}\nDescrição: {self.descricao}\nCoordenador: {self.coordenador}\nDocentes: {self.docentes}]"

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
    
    def __str__(self) -> str:
        return f'Matrícula: {self.matricula_a}\nNome: {self.nome_a}\nCPF: {self.cpf_a}\nEmail: {self.email_a}\nCursos: {self.cursos}'
