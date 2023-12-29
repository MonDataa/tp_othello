from Othello import Othello
from copy import deepcopy

class AI:
    def __init__(self):
        self.nb_situations_examinees = 0

    def compter_situations(self, init):
        if init:
            self.nb_situations_examinees = 1
        else:
            self.nb_situations_examinees += 1

    def tour_joueur_courant(self, prof_courante):
        return prof_courante % 2 == 1

    def min_max(self, othello, joueur, prof_courante, prof_max, heuristique):
        self.compter_situations(prof_courante == 1)
        if prof_courante > prof_max:
            return ([], heuristique(othello, joueur))
        else:
            possibilites = othello.liste_coups()
            if len(possibilites) == 0:
                return self.evaluer_passer_son_tour(othello, joueur, prof_courante, prof_max, heuristique)
            else:
                situations_possibles = map(lambda coup: (coup, othello.tenter_coup(coup)), possibilites)
                if self.tour_joueur_courant(prof_courante):
                    return self.retenir_meilleur_coup(situations_possibles, joueur, prof_courante, prof_max, heuristique)
                else:
                    return self.retenir_pire_coup(situations_possibles, joueur, prof_courante, prof_max, heuristique)

    def evaluer_passer_son_tour(self, othello, joueur, prof_courante, prof_max, heuristique):
        situation = Othello(othello)
        situation.changer_joueur()
        enchainement, recompense = self.min_max(situation, joueur, prof_courante+1, prof_max, heuristique)
        return (([None] + enchainement), recompense)

    def retenir_meilleur_coup(self, situations_possibles, joueur, prof_courante, prof_max, heuristique):
        meilleure_recompense = None
        enchainement_retenu = None
        for (coup, situation) in situations_possibles:
            liste_coups, recompense = self.min_max(situation, joueur, prof_courante+1, prof_max, heuristique)
            if meilleure_recompense is None or recompense > meilleure_recompense:
                meilleure_recompense = recompense
                enchainement_retenu = [coup] + liste_coups
        return enchainement_retenu, meilleure_recompense

    def retenir_pire_coup(self, situations_possibles, joueur, prof_courante, prof_max, heuristique):
        pire_recompense = None
        enchainement_retenu = None
        for (coup, situation) in situations_possibles:
            liste_coups, recompense = self.min_max(situation, joueur, prof_courante+1, prof_max, heuristique)
            if pire_recompense is None or recompense < pire_recompense:
                pire_recompense = recompense
                enchainement_retenu = [coup] + liste_coups
        return enchainement_retenu, pire_recompense
    
    def negamax(self, othello, joueur, prof_courante, prof_max, heuristique):
        if prof_courante > prof_max or othello.est_termine():
            return -heuristique(othello, joueur)

        meilleure_recompense = -float('inf')
        for coup in othello.liste_coups():
            othello_temp = deepcopy(othello)
            othello_temp.jouer_coup(*coup)
            recompense = -self.negamax(othello_temp, joueur, prof_courante + 1, prof_max, heuristique)
            meilleure_recompense = max(meilleure_recompense, recompense)

        return meilleure_recompense

    def evaluer_passer_son_tour_negamax(self, othello, joueur, prof_courante, prof_max, heuristique):
        situation = deepcopy(othello)
        situation.changer_joueur()
        enchainement, recompense = self.negamax(situation, joueur, prof_courante+1, prof_max, heuristique)
        return (([None] + enchainement), recompense)
    
    
    def alpha_beta(self, othello, joueur, prof_courante, prof_max, heuristique, alpha, beta):
        self.compter_situations(prof_courante == 1)
        if prof_courante > prof_max:
            return ([], heuristique(othello, joueur))
        else:
            possibilites = othello.liste_coups()
            if len(possibilites) == 0:
                return self.evaluer_passer_son_tour_alpha_beta(othello, joueur, prof_courante, prof_max, heuristique, alpha, beta)
            else:
                if self.tour_joueur_courant(prof_courante):
                    return self.retenir_meilleur_coup_alpha_beta(othello, possibilites, joueur, prof_courante, prof_max, heuristique, alpha, beta)
                else:
                    return self.retenir_pire_coup_alpha_beta(othello, possibilites, joueur, prof_courante, prof_max, heuristique, alpha, beta)

    def evaluer_passer_son_tour_alpha_beta(self, othello, joueur, prof_courante, prof_max, heuristique, alpha, beta):
        situation = deepcopy(othello)
        situation.changer_joueur()
        enchainement, recompense = self.alpha_beta(situation, joueur, prof_courante+1, prof_max, heuristique, alpha, beta)
        return (([None] + enchainement), recompense)

    def retenir_meilleur_coup_alpha_beta(self, othello, possibilites, joueur, prof_courante, prof_max, heuristique, alpha, beta):
        coup_retenu = None
        recompense_retenue = None
        enchainement_retenu = None
        for coup in possibilites:
            nouvelle_situation = deepcopy(othello)
            nouvelle_situation.jouer_coup(*coup)
            liste_coups, recompense = self.alpha_beta(nouvelle_situation, joueur, prof_courante+1, prof_max, heuristique, alpha, beta)
            if recompense_retenue is None or recompense > recompense_retenue:
                recompense_retenue = recompense
                enchainement_retenu = liste_coups
                coup_retenu = coup
                if recompense_retenue >= beta:
                    break
            if recompense > alpha:
                alpha = recompense
        return [coup_retenu] + enchainement_retenu, recompense_retenue

    def retenir_pire_coup_alpha_beta(self, othello, possibilites, joueur, prof_courante, prof_max, heuristique, alpha, beta):
        coup_retenu = None
        recompense_retenue = None
        enchainement_retenu = None
        for coup in possibilites:
            nouvelle_situation = deepcopy(othello)
            nouvelle_situation.jouer_coup(*coup)
            liste_coups, recompense = self.alpha_beta(nouvelle_situation, joueur, prof_courante+1, prof_max, heuristique, alpha, beta)
            if recompense_retenue is None or recompense < recompense_retenue:
                recompense_retenue = recompense
    
