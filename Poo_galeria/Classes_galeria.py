#socorro essa questao é muito grande e eu não vou saber fazer sozinha
class Artistas:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome
    
    @property
    def nacionalidade(self):
        return self._nacionalidade
        
    def imprimir(self):
        return(f'Nome: {self.nome}\nNacionalidade: {self.nacionalidade}')

class Obra:
    codigo = 0
    def __init__(self, dataAquisicao, titulo, tecnica, valor, autor: Artistas):
        self._codigo = __class__.codigo + 1
        __class__.codigo += 1
        self._dataAquisicao = dataAquisicao
        self._titulo = titulo
        self._tecnica = tecnica
        self._valor = 0
        self._autor = autor
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def dataAquisicao(self):
        return self._dataAquisicao
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def tecnica(self):
        return self._tecnica
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def autor(self):
        return self._autor
    
    def avaliar(self):
        tecnica = int(input('Qual a sua avaliação da técnica utilizada? [1]Boa\n[2]Inteeressante\n[5]Excelente'))
        inovacao = int(input('Qual a sua avaliação da inovação apresentada? [2]Comum\n[4]Inovadora\n[6]Única'))
        self._valor = (tecnica * 50 + inovacao * 80) * 10
        print(f'O valor da obra é: {self._valor}')
    
    def imprimir(self):
        return(f'Código da Obra: {self._codigo}\nTítulo da Obra: {self._titulo}\nAutor da Obra: {self._autor}\nTécnica utilizada: {self._tecnica}')
    
    def imprimirObra(self):
        return(f'Código da Obra: {self._codigo}\nTítulo da Obra: {self._titulo}\nValor da Obra: {self._valor}')
    
class Escultura(Obra):
    def __init__(self, dataAquisicao, titulo, tecnica, autor: Artistas, tp_material):
        super().__init__(dataAquisicao, titulo, tecnica, autor)
        self._tp_material = tp_material
    
    @property
    def tp_material(self):
        return self._tp_material
    
    def imprimir(self):
        return(f'Código da Escultura: {self._codigo}\nTítulo da Escultura: {self._titulo}\nAutor da Escultura: {self._autor}\nTécnica utilizada: {self._tecnica}\nTipo de material utilizado: {self._tp_material}')

class Pintura(Obra):
    def __init__(self, dataAquisicao, titulo, tecnica, autor: Artistas, tp_tinta):
        super().__init__(dataAquisicao, titulo, tecnica, autor)
        self._tp_tinta = tp_tinta
    
    @property
    def tp_tinta(self):
        return self._tp_tinta
    
    def imprimir(self):
        return(f'Código da Pintura: {self._codigo}\nTítulo da Pintura: {self._titulo}\nAutor da Pintura: {self._autor}\nTécnica utilizada: {self._tecnica}\nTipo de tinta utilizada: {self._tp_tinta}')

class Galeria:
    def __init__(self, nome, telefone, nm_resp) -> None:
        self._nome = nome
        self._telefone = telefone
        self._nm_resp = nm_resp
        self._pinturas = []
        self._esculturas = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def nm_resp(self):
        return self._nm_resp
    
    @property
    def pinturas(self):
        return self._pinturas
    @pinturas.setter
    def pinturas(self, obra:Pintura):
        self.pinturas.append(obra)
    
    @property
    def esculturas(self):
        return self._esculturas
    @esculturas.setter
    def esculturas(self, obra:Escultura):
        self.esculturas.append(obra)
    
    def pesquisarArtista(self, nome):
        for elemento in self.pinturas:
            if(elemento._autor.nome == nome):
                return elemento
        for elemento in self.esculturas:
            if(elemento._autor.nome == nome):
                return elemento
        return None

    def cadastrarPintura(self, autor: Artistas):
        dataAquisicao = input('Data: ')
        titulo = input('Título: ')
        tecnica = input('Técnica: ')
        autor = input('Autor: ')
        tp_tinta = input('Tipo de tinta: ')
        obra = input('Obra: ')
        self.pinturas = []

    def cadastrarEscultura(self, autor: Artistas):
        dataAquisicao = input('Data: ')
        titulo = input('Título: ')
        tecnica = input('Técnica: ')
        autor = input('Autor: ')
        tp_material = input('Tipo de material: ')
        obra = input('Obra: ')
        self.esculturas = []
    
    def cadastrarObra(self):
        nome = input('Qual o artista que procura?: ')
        artista = self.pesquisarArtista(nome)
        if artista == None:
            f"Artista não cadastrado. Cadastre-o agora."
            novo_cadastro = Artistas(nome, input('Qual é a nacionalidade do artista?'))
            artista = novo_cadastro
        
        tp_obra = int(input('Deseja cadastrar uma pintura [1] ou uma escultura [2]?'))

        if tp_obra == 1:
            self.cadastrarPintura(artista)
            f'Cadastro Realizado!'
        
        if tp_obra == 2:
            self.cadastrarEscultura(artista)
            f'Cadastro Realizado!'
        
    def pesquisarObras(self, nome):
        for elemento in self.pinturas:
            if (elemento._autor.nome == nome):
                print(elemento.imprimir())
        for elemento in self.esculturas:
            if (elemento._autor.nome == nome):
                print(elemento.imprimir())
    
    def pesquisarCodigo(self, codigo):
        for elemento in self.pinturas:
            if (elemento._autor.codigo == codigo):
                return elemento
        for elemento in self.esculturas:
            if (elemento._autor.codigo == codigo):
                return elemento
    
    def imprimirObras(self):
        for elemento in self.pinturas:
            return Pintura.imprimir()
        for elemento in self.esculturas:
            return Escultura.imprimir()
