class ListeChainee():
    def __init__(self):
        self.premier = None
        self.taille = 0
    
    def inserer(self, valeur):
        new = noeud(valeur)
        i  = 0

        if self.premier == None:
            self.premier = new
            self.taille += 1
        else :
            temp = self.premier
            new.suivant = temp
            self.premier = new
            self.taille += 1


    def supprimer(self):
    # Fonction qui supprime le premier élément de la liste 
        if self.taille ==0:
            return None
        else:
            temp = self.premier
            self.premier = self.premier.suivant
            self.taille -= 1
            return temp.valeur


    def rechercher(self, valeur):
        temp = self.premier
        while temp.valeur != valeur:
            temp = temp.suivant
        return temp

    def taille(self):
        return self.taille

    def est_vide(self):
        return self.taille == 0           
    
class noeud():
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None



