class Carte:

    cartes = []
    valeur = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V","d","R"]
    couleur = ["Carreau", "Coeur", "Pique", "Trèfle"]
    for c in couleur:
        for v in valeur:
            cartes.append([v + " de " + c])



