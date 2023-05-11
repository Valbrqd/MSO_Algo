import random as rd
import csv
import os
import GeneticTSPGui as gui

class Ville():
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = int(x)
        self.y = int(y)
    
    def distance_vers(self, ville):
        return ((self.x - ville.x)**2 + (self.y - ville.y)**2)**0.5
    
    def __str__(self):
        return self.nom
    
class Trajet():
    def __init__(self,lst= []):
        self.lstv = rd.sample(lst,len(lst))
        self.dist = self.calc_dist()
    
    def calc_dist(self):
        dist = 0
        for i in range(len(self.lstv)-1):
            
            dist += self.lstv[i].distance_vers(self.lstv[i+1])
        return dist
    
    def est_valide(self):
        for val in self.lstv:
            for val2 in self.lstv:
                if val == val2:
                    return False
        return True

    def __str__(self):
        return f"Trajet: {self.lstv} \nDistance: {self.dist}"
    
class Population():
    def __init__(self):
        self.pop = []

    def initialiser(self, taille, list_villes):
        for i in range(taille):
            self.pop.append(Trajet(list_villes))
    
    def ajouter(self, trajet):
        self.pop.append(trajet)

    def meilleur(self):
        best = self.pop[0]
        for trajet in self.pop:
            if trajet.dist < best.dist:
                best = trajet
        return best
    
    def bests(self):
        self.pop.sort(key = lambda x: x.dist)
    
        return self.pop[:10]
    
    def __str__(self) -> str:
        return f"Population: {self.pop}"
    

class PVC_Genetique:
    def __init__(self,lst, popsize = 40, gen = 100, elitisme = True, mutation = 0.3):
        self.ltsv = lst
        self.popsize = popsize
        self.gen = gen
        self.elitisme = elitisme
        self.mutation = mutation
        self.PVC = gui.PVC_Genetique_GUI(lst)

    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def croiser(self,p1,p2):
        e1 = Trajet()
        e2 = Trajet()
        done = []
        inter = rd.randint(1,len(p1.lstv))
        e1.lstv = p1.lstv[:inter]
        e2.lstv = p2.lstv[inter:]
        for i in range(len(e1.lstv)):
            if e1.lstv[i] in done :
                for ville_rempl in e2:
                    if ville_rempl not in done:
                        e1.lstv[i] = ville_rempl
                        done.append(ville_rempl)
                        break
            else:
                done.append(e1.lstv[i])
        e1.calc_dist()
        return e1
    
    def muter(self, trajet):
        i1 = rd.randint(0,len(trajet.lstv))
        i2 = rd.randint(0,len(trajet.lstv))
        trajet.lstv[i1],trajet.lstv[i2] = trajet.lstv[i2],trajet.lstv[i1]
        trajet.calc_dist()
        return trajet

    def selectionner(self, population):
        moy = 0
        for path in population.pop:
            moy += path.dist
        moy = moy/len(population.pop)
        for path in population.pop:
            if path.dist > moy:
                population.pop.remove(path)
        return population
    
    def evoluer(self, population):
        nb_init = len(population.pop)
        self.selectionner(population)
        while len(population.pop) < nb_init:
            if rd.random() < self.mutation:
                population.pop.append(self.muter(rd.choice(population.pop)))
            else:
                p1 = rd.choice(population.pop)
                p2 = rd.choice(population.pop)
                population.pop.append(self.croiser(p1,p2))
        return population

    def executer(self,afficher=True):
        self.clear_term()
        population = Population()
        population.initialiser(self.popsize,self.ltsv)
        for i in range(self.gen):
            population = self.evoluer(population)
            self.clear_term()
            print(f"Generation: {i}")
            print(f"Meilleur trajet: {population.meilleur()}")
            print(f"Meilleurs trajets: {population.bests()}")
        
        if afficher:
            self.PVC.afficher(population.meilleur(),population.meilleur(),afficher_noms=True)
        self.PVC.window.mainloop()
            

def generer_villes(self,nb_villes=20):
    list=[]
    for i in range(nb_villes):
        name = i
        x = rd.randint(0,300)
        y = rd.randint(0,300)
        
        list.append(Ville(i,x,y))

def lire_csv(file):
    lstV = []
    with open(f"TP8/{file}.csv","r") as fich:
        reader = csv.reader(fich, delimiter = ',')
        for row in reader:
            lstV.append(Ville(row[0],row[1],row[2]))
            
    return lstV

def main():
    a = PVC_Genetique(lire_csv("30"))

    a.executer()

    
if __name__ == "__main__":
    main()
            
        