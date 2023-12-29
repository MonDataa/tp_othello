class Piece:
    def __init__(self, couleur):
        assert couleur == "noir" or couleur== "blanc"
        self.couleur = couleur

    def __str__(self):
        if self.couleur == "noir":
            return "N"
        else:
            return "B"

    def flip(self):
        if self.couleur == "noir":
            self.couleur = "blanc"
        else:
            self.couleur = "noir"

    def est_opposee(self, couleur):
        return couleur != self.couleur

    def est_semblable(self, couleur):
        return couleur == self.couleur