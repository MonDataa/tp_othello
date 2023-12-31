from AI import AI
from Gui import Gui
from Heuristique import Heuristique
from Othello import Othello

def main():
    othello = Othello()
    gui = Gui(othello)
    ai = AI()

    print("Bienvenue dans Othello!")
    mode = gui.choisir_mode()

    if mode == "1":  # Humain vs AI
        couleur_joueur_humain = gui.choisir_couleur_joueur()
        joueur_humain = couleur_joueur_humain
        joueur_IA = "blanc" if joueur_humain == "noir" else "noir"
        heuristique_IA = gui.choisir_heuristique()
        algorithme_IA = gui.choisir_algorithme()
    else:  # AI vs AI
        print("Configuration pour l'IA noir:")
        heuristique_noir = gui.choisir_heuristique()
        algorithme_noir = gui.choisir_algorithme()
        print("Configuration pour l'IA blanc:")
        heuristique_blanc = gui.choisir_heuristique()
        algorithme_blanc = gui.choisir_algorithme()
        joueur_humain = None
        joueur_IA = "noir"

    profondeur_IA = 4

    with open("scores_othello.txt", "w") as file:
      while not othello.est_termine():
        if othello.joueur_courant == joueur_humain:
            # Affiche le plateau avec les mouvements possibles pour le joueur humain
            othello.afficher_plateau_avec_mouvements()
            gui.jouer_coup_humain(othello)
        else:
            if mode == "1":
                heuristique = heuristique_IA
                algorithme = algorithme_IA
            else:
                heuristique = heuristique_noir if joueur_IA == "noir" else heuristique_blanc
                algorithme = algorithme_noir if joueur_IA == "noir" else algorithme_blanc
            gui.jouer_coup_ai(othello, joueur_IA, profondeur_IA, heuristique, algorithme)

        print(othello)
        if mode != "1":
          joueur_IA = "noir" if joueur_IA == "blanc" else "blanc"

            # Calculer et enregistrer le score
        score = heuristique(othello, othello.joueur_courant)
        file.write(f"Score pour {othello.joueur_courant} = {score}\n")


    print("Jeu terminé!")

    compteur = othello.compter_pieces()
    print(f"Noirs: {compteur['noir']}, Blancs: {compteur['blanc']}")
    if compteur["noir"] > compteur["blanc"]:
        print("Le joueur Noir gagne!")
    elif compteur["blanc"] > compteur["noir"]:
        print("Le joueur Blanc gagne!")
    else:
        print("Match nul!")

    # Enregistrer les coups dans un fichier
    with open("historique_coups_othello.txt", "w") as file:
        for coup in othello.historique_coups:
            file.write(f"{coup}\n")

if __name__ == "__main__":
    main()