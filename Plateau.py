from Piece import Piece
from Case import Case
from copy import deepcopy
from functools import reduce


class Plateau:
    def __init__(self, source = None):
        if source is None:
            self.plateau = []
            for _ in range(8):
                ligne = []
                for _ in range(8):
                    ligne.append(Case())
                self.plateau.append(ligne)

            self.plateau[3][3].placer(Piece("noir"))
            self.plateau[4][4].placer(Piece("noir"))
            self.plateau[3][4].placer(Piece("blanc"))
            self.plateau[4][3].placer(Piece("blanc"))
        else:
            self.plateau = deepcopy(source.plateau)

    def get_case(self, ligne, colonne):
        return self.plateau[ligne][colonne]

    def get_piece(self, ligne, colonne):
        return self.get_case(ligne,colonne).get_contenu()

    def __str__(self):
        retour = "  0 1 2 3 4 5 6 7\n"
        retour += " " + "-" * 17 + "\n"
        num_ligne = 0
        for ligne in self.plateau:
            repr_ligne = reduce(lambda acc,case: acc + str(case) + "|",ligne,"|")
            retour += str(num_ligne) + repr_ligne + "\n"
            retour += " " + "-" * 17 + "\n"
            num_ligne += 1
        return retour