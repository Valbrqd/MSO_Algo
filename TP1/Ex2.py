class ListeChainee():
    def __init__(self):
        self.premier = None
        self.taille = 0
    
    def inserer(self, valeur,k):
        new = noeud(valeur)
        i  = 0

        if self.premier == None:
            self.premier = new
            self.taille += 1
        else : 
            temp = self.premier
            while self.premier.suivant != None or i == k:
                i += 1
                temp = temp.suivant
            new.suivant = temp.suivant
            temp.suivant = new
            self.taille += 1


    def supprimer(self, k):
        i = 1
        temp = self.premier
        while i < k:
            i += 1
            temp = temp.suivant
        temp.suivant = temp.suivant.suivant
        self.taille -= 1


    def rechercher(self, valeur):
        temp = self.premier
        while temp.valeur != valeur:
            temp = temp.suivant
        return temp

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


liste = ListeChainee()
liste.inserer(1,0)
liste.inserer("test",1)


print(liste.rechercher("test").valeur)
liste.supprimer(1)
print(liste.rechercher(1).valeur)
print(liste.taille)
print(liste.est_vide())
