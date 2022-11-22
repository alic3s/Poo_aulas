class Quadrilatero:
    def __init__(self, base, altura = None):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, base):
        self._base = base
    

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, altura):
        self._altura = altura
    

    def calcula_area(self) -> float:
        if self.altura != None:
            area = self.base * self.altura
            return area
        else:
            self.altura = self.base
            area = self.base ** 2
            return area
    
    
    def calcula_perimetro(self) -> float:
        if self.altura != None:
            perimetro = 2 * (self.base + self.altura)
            return perimetro
        else:
            self.altura = self.base
            perimetro = self.base * 4
            return perimetro
    
    def __str__(self):
        return f"Base: {self.base}\nAltura: {self.altura}"
    

class Losango(Quadrilatero):
    def __init__(self, l1, l2, l3, l4, diagonal_maior, diagonal_menor) -> float:
        self._l1 = l1
        self._l2 = l2
        self._l3 = l3
        self._l4 = l4
        self._diagonal_maior = diagonal_maior
        self._diagonal_menor = diagonal_menor
    
    @property
    def l1(self):
        return self._l1
    @l1.setter
    def l1(self, l1):
        self._l1 = l1

    
    @property
    def l2(self):
        return self._l2
    @l2.setter
    def l2(self, l2):
        self._l2 = l2


    @property
    def l3(self):
        return self._l3
    @l3.setter
    def l3(self, l3):
        self._l3 = l3

    
    @property
    def l4(self):
        return self._l4
    @l4.setter
    def l4(self, l4):
        self._l4 = l4
    

    @property
    def diagonal_maior(self):
        return self._diagonal_maior
    @diagonal_maior.setter
    def diagonal_maior(self, diagonal_maior):
        self._diagonal_maior = diagonal_maior
    

    @property
    def diagonal_menor(self):
        return self._diagonal_menor
    @diagonal_menor.setter
    def diagonal_menor(self, diagonal_menor):
        self._diagonal_menor = diagonal_menor
    

    def calcula_area(self) -> float:
        area = self.diagonal_maior * (self.diagonal_menor / 2)
        return area
    
    def calcula_perimetro(self) -> float:
        perimetro = self.l1 + self._l2 + self.l3 + self.l4
        return perimetro
    
    def __str__(self):
        return f"1º lado: {self.l1}\n2º lado: {self.l2}\n3º lado: {self.l3}\n4º lado: {self.l4}\nDiagonal maior: {self.diagonal_maior}\nDiagonal menor: {self.diagonal_menor}"
    

class Trapezio(Quadrilatero):
    def __init__(self, base_maior, base_menor, altura, lado1, lado2):
        self._base_maior = base_maior
        self._base_menor = base_menor
        self._altura = altura
        self._lado1 = lado1
        self._lado2 = lado2
    
    @property
    def lado1(self):
        return self._lado1
    @lado1.setter
    def lado1(self, lado1):
        self._lado1 = lado1
    

    @property
    def lado2(self):
        return self._lado2
    @lado2.setter
    def lado2(self, lado2):
        self._lado2 = lado2

    
    @property
    def base_maior(self):
        return self._base_maior
    @base_maior.setter
    def base_maior(self, base_maior):
        self._base_maior = base_maior
    

    @property
    def base_menor(self):
        return self._base_menor
    @base_menor.setter
    def base_menor(self, base_menor):
        self._base_menor = base_menor
    

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, altura):
        self._altura = altura
    

    def calcula_area(self) -> float:
        area = (self.base_maior + self.base_menor) * self.altura / 2
        return f'{area:.2f}'.format(area)
    
    def calcula_perimetro(self) -> float:
        perimetro = self.base_maior + self.base_menor + self.lado1 + self.lado2
        return perimetro
    
    def __str__(self):
        return f"1º lado: {self.lado1}\n2º lado: {self.lado2}\nBase maior: {self.base_maior}\nBase menor: {self.base_menor}\nAltura: {self.altura}"


#instanciar um quadrado
quadrado=Quadrilatero(10)
print('Area quadrado: ', quadrado.calcula_area())
print('Perímetro quadrado: ', quadrado.calcula_perimetro())
print(quadrado)
print()

#instanciar um retangulo
retangulo=Quadrilatero(4,5)
print(retangulo)
print('Area retângulo:', retangulo.calcula_area())
print('Perímetro retângulo:', retangulo.calcula_perimetro())
print()

#instanciar um trapezio
trapezio=Trapezio(4,5,8,10,15)
print(trapezio)
print('Area trapezio:', trapezio.calcula_area())
print('Perímetro trapezio:', trapezio.calcula_perimetro())
print()

#instanciar um losango
losango=Losango(8,8,8,8,12,7)
print(losango)
print('Area losango:', losango.calcula_area())
print('Perímetro losango:', losango.calcula_perimetro())
