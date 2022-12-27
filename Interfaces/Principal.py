from iFormaGeometrica import iFormaGeometrica
from Cilindro import Cilindro
from Poliedro import Poliedro


iFormaGeometrica.register(Poliedro)
iFormaGeometrica.register(Cilindro)

cilindro = Cilindro(2, 5)
print(cilindro)
