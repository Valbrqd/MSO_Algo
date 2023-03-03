class ListeChainee():
    def __init__(self):
        self.premier = None
        self.taille = 0
    
    def inserer(self, valeur,k):
        new = noeud(valeur)

        if self.premier == None:
            self.premier = new
        else : 
            temp = self.premier
            while self.premier.suivant != None:
                temp = temp.suivant
            temp.suivant = new

    def supprimer(self, k):
        pass

    def rechercher(self, k):
        pass

    def taille(self):
        return self.taille

    def est_vide(self):
        if self.taille == 0:
            return True
        else:
            return False
    


class noeud():
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None
