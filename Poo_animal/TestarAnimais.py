from animal import Animal
from mamifero import Mamifero
from peixe import Peixe

Camelo = Mamifero('Camelo', '150cm', 4, 'Amarelo', 'Terra', '2.0m/s', 'Plantas')

Tubarao = Peixe("Tubarão", '300cm', 0, 'Cinzento', 'Mar', '1.5m/s', 'Barbatanas e Cauda')

UrsoCanada = Mamifero('Urso-Do-Canadá', (str(180) + 'cm'), 4, 'Vermelho', 'Terra', (str(0.5) + 'm/s'), 'Mel')

print(UrsoCanada.dadosMamifero())
