from Piece import Piece
from Case import Case
from Plateau import Plateau
from copy import deepcopy
from functools import reduce

def rang_valide(rang):
    return 0 <= rang <= 7

DIRECTIONS = [(1,0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

class Othello:
    def __init__(self, source=None, adversaire_AI=True):
        self.historique_coups = []
        if source is None:
            self.plateau = Plateau()
            self.joueur_courant = "noir"
        else:
            self.plateau = Plateau(source.plateau)
            self.joueur_courant = source.joueur_courant
            self.adversaire_AI = adversaire_AI

    def changer_joueur(self):
        if self.joueur_courant == "noir":
            self.joueur_courant = "blanc"
        else:
            self.joueur_courant = "noir"

    def case_valide(self,x, y):
        if self.plateau.get_case(x,y).est_occupee():
            return False
        for dir in DIRECTIONS:
            if self.case_valide_direction(x, y, dir):
                return True
        return False

    def case_valide_direction(self, ligne, colonne, direction):
        ligne_courante = ligne + direction[0]
        colonne_courante = colonne + direction[1]
        valide = 0 <= ligne_courante <= 7 and \
                 0 <= colonne_courante <= 7 and \
                 self.plateau.get_case(ligne_courante, colonne_courante).est_occupee() and\
                 self.plateau.get_piece(ligne_courante, colonne_courante).est_opposee(self.joueur_courant)
        if not valide:
            return False
        while rang_valide(ligne_courante) and rang_valide(colonne_courante):
            if self.plateau.get_case(ligne_courante, colonne_courante).est_vide():
                return False
            elif self.plateau.get_piece(ligne_courante, colonne_courante).est_semblable(self.joueur_courant):
                return True
            ligne_courante += direction[0]
            colonne_courante += direction[1]
        return False

    def est_termine(self):
        # Vérifier si le plateau est plein
        plein = all(not case.est_vide() for ligne in self.plateau.plateau for case in ligne)
        if plein:
            return True

        # Vérifier si l'un des joueurs peut jouer un coup
        peut_jouer_noir = self.joueur_peut_jouer("noir")
        peut_jouer_blanc = self.joueur_peut_jouer("blanc")

        return not self.joueur_peut_jouer("noir") and not self.joueur_peut_jouer("blanc")

    def joueur_peut_jouer(self, couleur_joueur):
        couleur_temp = self.joueur_courant
        self.joueur_courant = couleur_joueur
        peut_jouer = any(self.case_valide(ligne, colonne) for ligne in range(8) for colonne in range(8))
        self.joueur_courant = couleur_temp
        return peut_jouer

    def jouer_coup(self, ligne, colonne):
        self.plateau.get_case(ligne, colonne).placer(Piece(self.joueur_courant))
        for dir in DIRECTIONS:
            if self.case_valide_direction(ligne, colonne, dir):
                self.retourner(ligne, colonne, dir)
        self.historique_coups.append((ligne, colonne))
        self.changer_joueur()

    def rejouer_partie(self):
        # Réinitialiser le jeu
        self.__init__()
        for coup in self.historique_coups:
            self.jouer_coup(*coup)
            print(self)  # Afficher le plateau après chaque coup
            # Vous pouvez ajouter une pause ou une interaction ici si nécessaire

    def retourner(self, ligne, colonne, direction):
        termine = False
        ligne_courante = ligne + direction[0]
        colonne_courante = colonne + direction[1]
        while not(termine):
            self.plateau.get_piece(ligne_courante, colonne_courante).flip()
            ligne_courante += direction[0]
            colonne_courante += direction[1]
            termine = not(rang_valide(ligne_courante)) or\
                      not(rang_valide(colonne_courante)) or \
                      self.plateau.get_piece(ligne_courante, colonne_courante).est_semblable(self.joueur_courant)

    def tenter_coup(self, coup):
        ligne = coup[0]
        colonne = coup[1]
        nouveau_jeu = Othello(self)
        nouveau_jeu.jouer_coup(ligne, colonne)
        return nouveau_jeu


    def liste_coups(self):
        resultat = []
        for ligne in range(8):
            for colonne in range(8):
                if self.case_valide(ligne, colonne):
                    resultat.append((ligne, colonne))
        return resultat

    def __str__(self):
        retour = "A " + self.joueur_courant + " de jouer\n"
        retour += str(self.plateau)
        return retour

    def compter_pieces(self):
        compteur = {"noir": 0, "blanc": 0}
        for ligne in self.plateau.plateau:
            for case in ligne:
                if case.est_occupee():
                    if case.get_contenu().couleur == "noir":
                        compteur["noir"] += 1
                    else:
                        compteur["blanc"] += 1
        return compteur