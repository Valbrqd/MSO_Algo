# On crée une classe qui représente un Noeud dans une liste chainée
class Noeud():
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None
    
    def __str__(self):
        return str(self.valeur)

# On crée une classe qui représente une liste chainée
class ListeChainee():
    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0

    def __str__(self):
        chaine = ""
        courant = self.tete
        while courant != None:
            chaine += str(courant) + " "
            courant = courant.suivant
        print(chaine)
    
    def inserer(self, valeur, position):
        nouveau = Noeud(valeur)
        if position == 0:
            nouveau.suivant = self.tete
            self.tete = nouveau
        else:
            courant = self.tete
            for i in range(position - 1):
                courant = courant.suivant
            nouveau.suivant = courant.suivant
            courant.suivant = nouveau
        self.taille += 1
    
    def supprimer(self, position):
        if position == 0:
            self.tete = self.tete.suivant
        else:
            courant = self.tete
            for i in range(position - 1):
                courant = courant.suivant
            courant.suivant = courant.suivant.suivant
        self.taille -= 1

    def rechercher(self, valeur):
        courant = self.tete
        position = 0
        while courant != None:
            if courant.valeur == valeur:
                return courant
            courant = courant.suivant
            position += 1
        return -1
    
    def index(self,valeur):
        courant = self.tete
        position = 0
        while courant != None:
            if courant.valeur == valeur:
                return position
            courant = courant.suivant
            position += 1
        return -1
    
    def taille(self):
        return self.taille
    
    def estVide(self):
        return self.taille == 0
    
maLst = ListeChainee()
for i in range(41):
    maLst.inserer(i+1, i)

maLst.rechercher(41).suivant = maLst.rechercher(1)

def josephus(lst):
    courant = lst.tete
    while lst.taille > 1:
        lst.supprimer(lst.index(courant.suivant.suivant.valeur))
        courant = courant.suivant.suivant
    return lst.tete.valeur

print(josephus(maLst))