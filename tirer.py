from random import *

class Tirer:

    def __init__(self, cartes):
        self.cartes = cartes

    def tirer(self):
        n = randint(1,52)
        Carte_tirée = self.cartes[n]
        self.cartes.pop(n)
        print("La carte que vous avez tirée est la suivante: ", Carte_tirée)


