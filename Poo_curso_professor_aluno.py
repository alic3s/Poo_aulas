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
        texto = 'Código: {0}\nNome: {1}\nDescrição{3}'.format(self.codigo, self.nome, self.descricao)
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
        self.dt_admissao = dt_admissao
        self.email = email
        self._lotacao = curso_lotacao

    @property
    def lotacao(self, curso):
        return self._lotacao

    @lotacao.setter
    def lotacao(self, curso):
        self._lotacao = curso
        
    def __str__(self):
        texto = 'Matrícula: {0}\nNome: {1}\nCPF: {2}\nData de Admissão: {3}\nEmail: {4}\
            Lotação: {5}'.format(self.matricula, self.nome, self.cpf, self.dt_admissao,\
                self.email, self._lotacao.nome)
        return texto
    
    @staticmethod
    def gerarMatricula():
        ano = str(date.today().year)
        mes = str(date.today().month)
        registro = str(randint(1000,9999))
        return ano + mes + registro



class Aluno:
    def __init__(self, matricula, nome, cpf, email = None):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self._cursos = []
    
    @staticmethod
    def gerarMatricula():
        ano = str(date.today().year)
        mes = str(date.today().month)
        registro = str(randint(1000,9999))
        return ano + mes + registro
    
    @property
    def cursos(self):
        return self._cursos
    
    @cursos.setter
    def cursos(self, cursos):
        self.cursos.append(cursos)
    
    def __str__(self):
        texto = 'Matrícula: {}\n'.format(self.matricula)+\
            "Nome: {}\n".format(self.nome)+\
                'CPF: {}\n'.format(self.cpf)+\
                    'Email: {}\n'.format(self.email)
        textoCursos = 'Os cursos que o aluno está matriculado são: '
        for elemento in self.cursos:
            textoCursos = textoCursos+', '+elemento.nome
        return texto + textoCursos
