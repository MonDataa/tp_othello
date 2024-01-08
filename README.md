# Rapport sur le Jeu Othello

## Sommaire
1. **Introduction**
2. **Analyse**
   - a. Modélisation et Structures de Données
   - b. Algorithmes Principaux
3. **Validation**
   - a. Résultats Numériques
   - b. Comparaison des Stratégies
4. **Discussion**
   - a. Efficacité des Stratégies
   - b.	Difficultés et Limites
5. **Conclusion**
6. **Appendices**
   - a.	Code Source
7. **Bibliography**

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
Des tests ont été réalisés pour mesurer l'efficacité des algorithmes en termes de temps de calcul et de nombre de nœuds générés. Principaux résultats :
- Avec une profondeur de 4, l'algorithme Alpha-beta réduit considérablement le temps de calcul par rapport à Min-Max et Nega-Max.

#### Performance des Stratégies
Les performances comparatives de différentes stratégies utilisant Alpha-beta ont donné les résultats suivants :
- **Coins valorisés >. Absolue:** Noirs - 30, Blancs - 34
- **Mixte >. Mobilité:** Noirs - 37, Blancs - 27
- **Mobilité >. Absolue:** Noirs - 33, Blancs - 31
- **Mobilité >. Coins valorisés:** Noirs - 42, Blancs - 22
- **Absolue >. Mixte:** Noirs - 31, Blancs - 33
- **Coins valorisés >. Mixte:** Noirs - 44, Blancs - 20
- **Positionnelle >. Mobilité:** Noirs - 19, Blancs - 45
- **Positionnelle >. Absolue:** Noirs - 29, Blancs - 35
- **Positionnelle >. Coins Absolue:** Noirs - 11, Blancs - 53
- **Positionnelle >. Mixte:** Noirs - 24, Blancs - 40


#### Comparaison des Stratégies

La comparaison des stratégies d'IA dans le jeu Othello indique des tendances distinctes. La stratégie de Coins valorisés surpasse souvent l'Heuristique Absolue, suggérant une efficacité accrue en valorisant les pièces stratégiques dans les coins. De même, l'Heuristique de Mobilité a montré une performance supérieure contre l'Absolue et même contre la stratégie de Coins valorisés, mettant en avant l'importance de la flexibilité et du contrôle du jeu. Toutefois, l'Heuristique Mixte, bien qu'équilibrée, semble moins performante face à d'autres stratégies. Cela suggère que l'adaptation des poids dans cette stratégie mixte est cruciale pour son efficacité. En résumé, chaque stratégie a ses forces et faiblesses distinctes, et leur efficacité peut varier en fonction du contexte de jeu.

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

Ce projet d'Othello en IA démontre l'efficacité et la complexité des algorithmes Min-Max, Alpha-Beta et Nega-Max dans la stratégie du jeu. La modélisation et la structuration des données ont joué un rôle clé dans une simulation réaliste. Bien que l'efficacité des stratégies d'IA soit prouvée, le projet révèle des défis d'implémentation et des limites algorithmiques. Cependant, il représente un progrès significatif dans l'application de l'IA aux jeux de stratégie, avec des améliorations potentielles par l'apprentissage par renforcement et l'optimisation des calculs

### Annexes
#### Code Source
- [Final Version](https://github.com/MonDataa/tp_othello)

### Bibliographie
- [Stanford CS221 Autumn 2019](https://stanford-cs221.github.io/autumn2019/#schedule)

