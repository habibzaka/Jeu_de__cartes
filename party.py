from melanger import *
from carte import *
from tirer import *

class Party:
        
  #  def __init__(self, in_put,cartes):
    #    self.in_put = in_put
    #    self.cartes = cartes

    def party(self):
        print("----------------------------------------------------")
        print("----Bonjour, bien venue dans votre jeu de cartes----")
        print("----------------------------------------------------")
        continuer = True
        while continuer:
            Action = input("Que vous les faire maintenant?\n  1-pour tirer une carte, taper 'tirer',\n  2-pour mélanger les cartes, taper 'melanger'\n  3-pour quitter, taper'recommencer'\n  4-pour quitter, taper'quitter'\n")
            print("----------------------------------------------------")
            c=Carte()
            t=Tirer(c.cartes)
            m=Melanger(c.cartes)
            if Action == "tirer":
                t.tirer()
            elif Action == "melanger":
                m.melanger()
            elif Action == "quitter":
                continuer = False
                print("Au revoir")
            elif Action == "recommencer":
                print("Vous avez recommencer le jeu\n")
            else: 
                print("je ne comprends pas ce que vous dites, désolé, ressayer")
                choix = input("Pour recommencer, taper 'recommencer'\n")
                if choix == "recommencer":
                    print("Vous avez recommencer le jeu\n")
                else:
                    continuer = False
