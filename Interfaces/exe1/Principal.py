from iFormaGeometrica import iFormaGeometrica
from Cilindro import Cilindro
from Poliedro import Poliedro


iFormaGeometrica.register(Poliedro)
iFormaGeometrica.register(Cilindro)

cili = Cilindro(2, 5)
print(cili)

poliedro = Poliedro(4,8,8,10,12,9)
print(poliedro)
