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


    def rechercher(self):
        return self.premier.valeur

    def taille(self):
        return self.taille

    def est_vide(self):
        return self.taille == 0           
    
class noeud():
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

with open("TP1/ex3.txt", "r") as fichier:
    # Lire chaque ligne et les stocker dans une liste
    lignes = fichier.readlines()
    fichier.close()

liste = ListeChainee()
dic = {"{": "}", "(": ")", "[": "]", "<": ">"}
for ligne in lignes : 
    for val in ligne: 
        if val in dic.keys():
            liste.inserer(val)
        elif not liste.est_vide() or dic[liste.rechercher()] == val:
            liste.supprimer()
        
        

print(liste.est_vide())
if liste.est_vide():
    print("Pas de probleme de parentheses")
else:
    print("Probleme de parentheses")

print(lignes)
