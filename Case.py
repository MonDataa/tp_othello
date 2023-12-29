class Case:
    def __init__(self):
        self.contenu = None

    def placer(self,piece):
        self.contenu = piece

    def flip(self):
        assert self.contenu != None
        self.contenu.flip()

    def est_occupee(self):
        return self.contenu != None

    def est_vide(self):
        return self.contenu is None

    def get_contenu(self):
        return self.contenu

    def __str__(self):
        if self.contenu is None:
            return " "
        else:
            return str(self.contenu)