from AI import AI
from Heuristique import Heuristique

class Gui:
    def __init__(self, othello):
        self.othello = othello
        self.ai = AI()

    def choisir_mode(self):
        mode = input("Choisissez le mode de jeu (1: Humain vs AI, 2: AI vs AI): ")
        return mode.strip()

    def choisir_algorithme(self):
        print("Choisissez l'algorithme pour l'AI:")
        print("1: Min-Max")
        print("2: NegaMax")
        print("3: Alpha-Beta")
        choix = input("Votre choix: ")
        if choix == "1":
            return self.ai.min_max
        elif choix == "2":
            return self.ai.negamax 
        elif choix == "3":
            return self.ai.alpha_beta 
        else:
            print("Choix invalide, utilisation de Min-Max par défaut.")
            return self.ai.min_max

    def choisir_heuristique(self):
        print("Choisissez l'heuristique pour l'AI:")
        print("1: Heuristique absolue")
        print("2: Heuristique Coins valorisés")
        print("3: Heuristique positionnelle")
        print("4: Heuristique de mobilité")
        print("5: Heuristique mixte")
        choix = input("Votre choix: ")
        if choix == "1":
            return Heuristique.heuristique_absolue  
        elif choix == "2":
            return Heuristique.heuristique_coins_valorises
        elif choix == "3":
            return Heuristique.heuristique_positionnelle
        elif choix == "4":
            return Heuristique.heuristique_mobilite 
        elif choix == "5":
            return Heuristique.heuristique_mixte 
        else:
            print("Choix invalide, utilisation de l'heuristique de mobilité par défaut.")
            return Heuristique.heuristique_mobilite

    def jouer_coup_humain(self, othello):
        coup_valide = False
        while not coup_valide:
            try:
                ligne, colonne = map(int, input("Entrez votre coup (ligne, colonne): ").split())
                if self.othello.case_valide(ligne, colonne):
                    self.othello.jouer_coup(ligne, colonne)
                    coup_valide = True
                else:
                    print("Coup invalide. Réessayez.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer deux nombres.")

    """def jouer_coup_ai(self, joueur, profondeur, heuristique, algorithme):
        print(f"L'IA ({joueur}) réfléchit...")
        solution = algorithme(self.othello, joueur, 1, profondeur, heuristique)
        coup_IA = solution[0][0]
        if coup_IA is None:
            self.othello.changer_joueur()
        else:
            self.othello.jouer_coup(coup_IA[0], coup_IA[1])"""

    def jouer_coup_ai(self,othello, joueur, profondeur, heuristique, algorithme):
        print(f"L'IA ({joueur}) réfléchit...")
        if algorithme == self.ai.alpha_beta:
            solution = self.ai.alpha_beta(othello, joueur, 1, profondeur, heuristique, -float('inf'), float('inf'))
        elif algorithme == self.ai.negamax:
            solution = self.ai.negamax(othello, joueur, 1, profondeur, heuristique)
        else:  # min_max ou autre algorithme
            solution = self.ai.min_max(othello, joueur, 1, profondeur, heuristique)

        # Gérer le retour des fonctions
        if isinstance(solution, tuple):
            coup_IA = solution[0][0] if solution[0] else None
        else:
            coup_IA = None

        if coup_IA:
            othello.jouer_coup(coup_IA[0], coup_IA[1])
        else:
            othello.changer_joueur()

    """def choisir_couleur_joueur(self):
        choix = input("Choisissez la couleur pour le joueur humain (1: Noir, 2: Blanc): ")
        return "noir" if choix == "1" else "blanc" """
    
    def choisir_couleur_joueur(self):
        while True:
            choix = input(" (1,bot IA : Noir) -> Choisissez la couleur Blanc pour le joueur humain (2,joueur humain: Blanc): ")
            if choix == "1":
                return "noir"
            elif choix == "2":
                return "blanc"
            else:
                print("Choix invalide. Veuillez choisir 2 pour Blanc.")
