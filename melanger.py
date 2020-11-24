from random import shuffle

class Melanger:
     
    def __init__(self, cartes):
        self.cartes = cartes

    def melanger(self):
        if len(self.cartes) < 52:
            raise(1, "Vous ne pouvez pas mélamger les cartes, vous avez déjà tirer une carte")
        else:
            shuffle(self.cartes)
        print("cartes mélanger")


