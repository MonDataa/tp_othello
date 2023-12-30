class Heuristique:
    @staticmethod
    def est_coin(ligne, colonne):
        return (ligne == 0 or ligne == 7) and (colonne == 0 or colonne == 7)

    @staticmethod
    def heuristique_absolue(othello, joueur):
        valeur = 0
        for ligne in range(8):
            for colonne in range(8):
                case = othello.plateau.get_case(ligne, colonne)
                if case.est_occupee():
                    piece = case.get_contenu()
                    if piece.est_semblable(joueur):
                        valeur += 1
                    else:
                        valeur -= 1
        return valeur

    @staticmethod
    def heuristique_coins_valorises(othello, joueur):
        valeur = 0
        for ligne in range(8):
            for colonne in range(8):
                case = othello.plateau.get_case(ligne, colonne)
                if case.est_occupee():
                    piece = case.get_contenu()
                    if piece.est_semblable(joueur):
                        valeur += 5 if Heuristique.est_coin(ligne, colonne) else 1
                    else:
                        valeur -= 5 if Heuristique.est_coin(ligne, colonne) else 1
        return valeur

    @staticmethod
    def heuristique_positionnelle(othello, joueur):
        poids = [[4, -3, 2, 2, 2, 2, -3, 4],
                 [-3, -4, -1, -1, -1, -1, -4, -3],
                 [2, -1, 1, 0, 0, 1, -1, 2],
                 [2, -1, 0, 1, 1, 0, -1, 2],
                 [2, -1, 0, 1, 1, 0, -1, 2],
                 [2, -1, 1, 0, 0, 1, -1, 2],
                 [-3, -4, -1, -1, -1, -1, -4, -3],
                 [4, -3, 2, 2, 2, 2, -3, 4]]
        valeur = 0
        for ligne in range(8):
            for colonne in range(8):
                case = othello.plateau.get_case(ligne, colonne)
                if case.est_occupee():
                    piece = case.get_contenu()
                    if piece.est_semblable(joueur):
                        valeur += poids[ligne][colonne]
                    else:
                        valeur -= poids[ligne][colonne]
        return valeur

    @staticmethod
    def heuristique_mobilite(othello, joueur):
        mobilite_joueur = len(othello.liste_coups()) if othello.joueur_courant == joueur else 0
        othello.changer_joueur()
        mobilite_adversaire = len(othello.liste_coups()) if othello.joueur_courant != joueur else 0
        othello.changer_joueur()
        return mobilite_joueur - mobilite_adversaire

    @staticmethod
    def heuristique_mixte(othello, joueur, poids_mobilite=0.5, poids_absolu=0.5):
        score_absolu = Heuristique.heuristique_absolue(othello, joueur)
        score_mobilite = Heuristique.heuristique_mobilite(othello, joueur)
        return poids_mobilite * score_mobilite + poids_absolu * score_absolu
