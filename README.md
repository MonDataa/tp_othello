# Rapport sur le Jeu Othello

## Sommaire
1. **Introduction**
2. **Analyse**
   a. Modélisation et Structures de Données
   b. Algorithmes Principaux
3. **Validation**
   a. Résultats Numériques
   b. Comparaison des Stratégies
4. **Discussion**
   a. Efficacité des Stratégies
   b. Difficultés et Limites
5. **Conclusion**
6. **Annexes**
   a. Code Source
7. **Bibliographie**

### Introduction
Ce rapport présente une analyse détaillée du jeu Othello, implémenté en Python. Nous discutons de la modélisation du jeu, des algorithmes développés pour l'intelligence artificielle (IA), et des résultats obtenus lors de différentes simulations.

### Analyse
#### Modélisation et Structures de Données
Othello est un jeu de stratégie sur un plateau 8x8, joué avec des pièces de couleurs opposées. Voici les composants clés modélisés en Python :

- **Piece:** Représente une pièce du jeu avec sa couleur.
- **Case:** Désigne une case du plateau, pouvant contenir une pièce.
- **Plateau:** Gère l'état actuel du jeu.
- **Othello:** Coordonne le déroulement du jeu, les changements de joueurs, et vérifie la fin de la partie.
- **Heuristique:** Stratégies utilisées (absolu, positionnel, mobilité, mixte).
- **AI:** Algorithmes utilisés (min-max, nega-max, alpha-beta) et leur évaluation.
- **GUI:** Méthodes pour les interfaces du jeu (version console).

#### Algorithmes Principaux
Nous avons implémenté plusieurs algorithmes pour l'intelligence artificielle (IA) dans le jeu Othello :

- **Min-Max et Alpha-Beta:** Ces algorithmes permettent de choisir le meilleur coup en anticipant les réponses de l'adversaire. Ils sont essentiels pour la prise de décision stratégique dans le jeu.
- **Nega-Max:** Il s'agit d'une variante simplifiée de l'algorithme Min-Max, également utilisée pour optimiser les décisions de jeu.

### Validation
#### Résultats Numériques
Les tests ont été réalisés pour mesurer l'efficacité des algorithmes en termes de temps de calcul et nombre de nœuds générés. Les résultats indiquent : 

Avec une profondeur de 4 Alpha-beta prend beaucoup moins de temps de calcul par rapport aux min-max et nega-max.


#### Comparaison des Stratégies
Nous avons comparé les performances des différentes stratégies IA contre un joueur humain ainsi qu'entre elles. Les résultats montrent que la stratégie absolue et la stratégie absolue améliorer (Coins valorisés) marche mieux que les autres peut import l’algorithme utilisé.

### Discussion
#### Efficacité des Stratégies

##### Heuristique Absolue
- **Concept:** Compte le nombre net de pièces du joueur par rapport à l'adversaire.
- **Efficacité:** Basique, efficace en fin de partie pour le nombre total de pièces, moins en début et milieu de partie.

##### Heuristique (Coins valorisés)
- **Concept:** Similaire à l'heuristique absolue, avec une valeur supplémentaire aux pièces dans les coins.
- **Efficacité:** Plus efficace que l'heuristique absolue, valorise les pièces incontestables dans les coins.

##### Heuristique Positionnelle
- **Concept:** Évalue les pièces selon leur position, avec un système de pondération.
- **Efficacité:** Avancée, efficace en début et milieu de partie pour le placement stratégique des pièces.

##### Heuristique de Mobilité
- **Concept:** Évalue la position selon la mobilité du joueur et de l'adversaire.
- **Efficacité:** Encourage le maintien de flexibilité et contrôle du jeu.

##### Heuristique Mixte
- **Concept:** Combinaison de l'heuristique absolue et de la mobilité, avec des poids ajustables.
- **Efficacité:** Équilibrée, adaptable à différents stades du jeu.

##### Interprétation Globale
- **Début de Partie:** Heuristiques positionnelle et de mobilité favorisées.
- **Milieu de Partie:** Combinaison des heuristiques positionnelle et de mobilité.
- **Fin de Partie:** L'heuristique absolue devient cruciale.

#### Difficultés et Limites
Parmi les difficultés rencontrées, c’était au niveau implémentation des algorithmes et développer la logique de jeu en général, ainsi l’interprétation des résultats.

En termes de limites, l'IA actuelle c’est qu’on a utilisé que les algorithmes IA classique au lieu d’ajouter la partie apprentissage par renforcement, le deuxième inconvénient c’est le langage en termes de calcul il prend plus temp d’exécution par rapport au langage comme java et c++.

Mais il reste possible d’utilisé un compilateur c pour exécuter python, ou utilisé un environnement GPU qui est gratuit dans le notebook (google colab)


### Conclusion
[Concluding remarks on the project.]

### Annexes
#### Code Source
- [Final Version](https://github.com/MonDataa/tp_othello)

### Bibliographie
- [Stanford CS221 Autumn 2019](https://stanford-cs221.github.io/autumn2019/#schedule)

