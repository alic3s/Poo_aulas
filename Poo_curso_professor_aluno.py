from datetime import date
from random import randint

class Curso:
    def __init__(self, codigo, nome, descricao, coordenador):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self._coordenador = None
        self._docentes = []
    
    @property
    def coordenador(self):
        return self._coordenador
    
    @coordenador.setter
    def coordenador(self, professor):
        self._coordenador = professor
    
    @property
    def docentes(self):
        return self._docentes

    @docentes.setter
    def docentes (self, professor):
        self.docentes.append(professor)

    def __str__ (self):
        texto = f'Código: {0}\nNome: {1}\nDescrição{3}'.format(self.codigo, self.nome, self.descricao)
        if self.coordenador is not None:
            texto += '\nCoordenador: {}\n'.format(self.coordenador.nome)
        textoDocentes = 'Docentes: \n'
        if self._docentes is not None:
            for elemento in self.docentes:
                textoDocentes = textoDocentes + '\n' + elemento.nome
        return texto + textoDocentes

class Professor:
    def __init__(self, nome, cpf, dt_admissao, curso_lotacao, email = None):
        self.matricula = __class__.gerarMatricula()
        self.nome = nome
        self.cpf = cpf
        self.admissao = dt_admissao
        self.email = email
        self._lotacao = curso_lotacao

    @property
    def lotacao(self, curso):
        return self._lotacao

    @lotacao.setter
    def lotacao(self, curso):
        self._lotacao = curso
        
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
