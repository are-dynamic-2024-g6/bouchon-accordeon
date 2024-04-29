# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

reaction_copieur = {
    (0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4, (0, 5): 5,
    (1, -1): 0, (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 4, (1, 4): 5,
    (2, -2): 0, (2, -1): 1, (2, 0): 2, (2, 1): 3, (2, 2): 4, (2, 3): 5,
    (3, -3): 0, (3, -2): 1, (3, -1): 2, (3, 0): 3, (3, 1): 4, (3, 2): 5,
    (4, -4): 0, (4, -3): 1, (4, -2): 2, (4, -1): 3, (4, 0): 4, (4, 1): 5,
    (5, -5): 0, (5, -4): 1, (5, -3): 2, (5, -2): 3, (5, -1): 4, (5, 0): 5
}

reaction_prudent = {
    (0, 0): 0, (0, 1): 1, (0, 2): 1, (0, 3): 2, (0, 4): 3, (0, 5): 4,
    (1, -1): 0, (1, 0): 0, (1, 1): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4,
    (2, -2): 0, (2, -1): 0, (2, 0): 1, (2, 1): 2, (2, 2): 3, (2, 3): 4,
    (3, -3): 0, (3, -2): 0, (3, -1): 1, (3, 0): 2, (3, 1): 3, (3, 2): 4,
    (4, -4): 0, (4, -3): 0, (4, -2): 1, (4, -1): 2, (4, 0): 3, (4, 1): 4,
    (5, -5): 0, (5, -4): 0, (5, -3): 1, (5, -2): 2, (5, -1): 3, (5, 0): 4
}






class Voiture:
    def __init__(self, position = None, conducteur = None, name = None , currentmove = 0  ):
        self.position = position
        self.conducteur = conducteur
        self.currentmove = currentmove
        self.name = name



def creer_monde(taille, pourcentage_voitures, pourcentage_de_copieur):
    monde = []
    classe_voiture = []
    nombres_voitures = int(taille * pourcentage_voitures)
    cptnbcopieur=0
    
    for i in range(nombres_voitures):
        
        if cptnbcopieur/nombres_voitures < pourcentage_de_copieur:
            monde.append(Voiture(i ,"C", "V" + str((nombres_voitures-1) - i)))
            classe_voiture.append("C")
            cptnbcopieur +=1
            
        else :
            monde.append(Voiture(i ,"P","V" + str((nombres_voitures-1) - i)))
            classe_voiture.append("P")
        
    
    for elem in monde:
        elem.conducteur = random.choice(classe_voiture)
        classe_voiture.pop(classe_voiture.index(elem.conducteur))
    
    
    monde[-1].conducteur = "SPECIAL"
    
    return monde
        


def deplacement(monde,vitesse,taille):
    temp_last = 0 
    distance = 0
    
    for elem in reversed(monde):
        
        
        if elem.conducteur == "SPECIAL":
            
            if elem.position < monde[0].position:
                distance = abs(monde[0].position - elem.position)
            elif elem.position >= monde[0].position:
                distance = abs((monde[0].position + taille) - elem.position)                
            if vitesse > distance:
                elem.currentmove = (distance - 1)
                
            else :
               elem.currentmove = vitesse
        
            temp_last = elem.currentmove
            elem.position = (elem.position + elem.currentmove) % taille

        
        else:
            if elem.conducteur == "C":
                elem.currentmove = reaction_copieur[(elem.currentmove, temp_last - elem.currentmove)]
                elem.position = (elem.position + elem.currentmove) % taille

            elif elem.conducteur == "P":
                elem.currentmove = reaction_prudent[(elem.currentmove, temp_last - elem.currentmove)]
                elem.position = (elem.position + elem.currentmove) % taille
            
            
            temp_last = elem.currentmove
    
    return monde


def nb_bouchons(monde, taille):
    bouchons = 0
    i = 0
    cpt = 1
    
    while i < taille - 1:
        # Calcul de la différence de position en tenant compte de la boucle
        diff_position = (monde[(i+1) % taille].position - monde[i].position) % taille
        
        if diff_position == 1:  # Voitures collées
            i += 1
            sum_vitesse = monde[i].currentmove
            
            # Recherche des voitures suivantes collées
            while i < taille - 1 and (monde[(i+1) % taille].position - monde[i].position) % taille == 1:
                i += 1
                cpt += 1
                sum_vitesse += monde[i].currentmove
            
            # Calcul de la moyenne de vitesse
            moyenne_vitesse = sum_vitesse / cpt
            
            # Vérification si la moyenne de vitesse est inférieure ou égale à 2 (bouchon)
            if moyenne_vitesse <= 1:
                bouchons += 1
            
            cpt = 1
        
        i += 1
        
    return bouchons



def distance_moyenne_entre_voitures(monde):
    distances = []
    taille = len(monde)
    
    for i in range(taille):
        # Calcul de la différence de position en tenant compte de la boucle
        diff_position = (monde[(i + 1) % taille].position - monde[i].position) % taille
        distances.append(diff_position)
    
    distance_moyenne = np.mean(distances)  # Calcul de la moyenne des distances
    return distance_moyenne



def taux_arret_voitures(monde):
    nb_voitures_totales = len(monde)
    nb_voitures_arretees = sum(1 for voiture in monde if voiture.currentmove == 0)
    
    if nb_voitures_totales == 0:
        return 0
    else:
        return (nb_voitures_arretees / nb_voitures_totales) * 100




def afficher(monde,taille) :
    
    temp_monde = [None]*taille
    print(50*"-")
    for elem in monde :
        temp_monde[elem.position] = elem      
    
    print("État du monde:")
    for i, voiture in enumerate(temp_monde):
        if voiture is not None:
            print(f"Position {i}: {voiture.position}, {voiture.conducteur},{voiture.name}, {voiture.currentmove}")
        else:
            print(f"Position {i}: Vide")


def generer_sequence_vitesses(nb_tours):
    sequence = []
    vitesse_max = 5
    vitesse_min = 0
    croissant = True
    
    for _ in range(nb_tours):
        if croissant:
            min_vitesse = min(sequence[-1] + 1, vitesse_max) if sequence else vitesse_min
            sequence.append(random.randint(min_vitesse, vitesse_max))
            croissant = False
        else:
            max_vitesse = max(sequence[-1] - 1, vitesse_min) if sequence else vitesse_max
            sequence.append(random.randint(vitesse_min, max_vitesse))
            croissant = True
    
    return sequence


def simulation(taille,pourcentage_voitures,pourcentage_de_copieur,nb_tours):
    monde_cree = creer_monde(taille, pourcentage_voitures, pourcentage_de_copieur)
    sequence = generer_sequence_vitesses(nb_tours)

    for vitesse in sequence:
        for i in range(4):
            
            monde_cree = deplacement(monde_cree, vitesse , taille)
            
    print("Vitesse actuel",vitesse)
    print("Nombre de bouchons :",nb_bouchons(monde_cree,len(monde_cree)))
    print("Ecart type entre les voitures :",round(distance_moyenne_entre_voitures(monde_cree)))
    print("Taux d'arrêt des voitures :", round(taux_arret_voitures(monde_cree)), "%")
        
    return (nb_bouchons(monde_cree,len(monde_cree)),taux_arret_voitures(monde_cree),distance_moyenne_entre_voitures(monde_cree))


# Définition des paramètres
taille_monde = 50
pourcentage_voitures = 0.8
pourcentages_de_copieur = [0,0.2,0.4,0.6,0.8,1.0]

# Liste pour stocker les résultats de chaque métrique
nb_bouchon_liste = []
taux_arret_liste = []
ecart_type_liste = []

# Calcul et stockage des résultats pour chaque pourcentage de copieurs
for elem in pourcentages_de_copieur:
    monde = simulation(taille_monde, pourcentage_voitures, elem, 5)
    nb_bouchon_liste.append(monde[0])
    taux_arret_liste.append(monde[1])
    ecart_type_liste.append(monde[2])
    



fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Graphique pour le nombre de bouchons
ax1.plot(pourcentages_de_copieur, nb_bouchon_liste, marker='o')
ax1.set_title('Nombre de bouchons')
ax1.set_xlabel('Taux de copieurs')
ax1.set_ylabel('Nombre de bouchons')
ax1.grid(True)
ax1.text(0.5, 1.05, f'Taille du monde: {taille_monde}, Pourcentage de voitures: {pourcentage_voitures}',
         horizontalalignment='center', transform=ax1.transAxes)

# Graphique pour le taux d'arrêt
ax2.plot(pourcentages_de_copieur, taux_arret_liste, marker='o')
ax2.set_title('Pourcentagex d\'arrêt')
ax2.set_xlabel('Taux de copieurs')
ax2.set_ylabel('Taux d\'arrêt des voitures (%)')
ax2.grid(True)
ax2.text(0.5, 1.05, f'Taille du monde: {taille_monde}, Pourcentage de voitures: {pourcentage_voitures}',
         horizontalalignment='center', transform=ax2.transAxes)

# Graphique pour l'écart type
ax3.plot(pourcentages_de_copieur, ecart_type_liste, marker='o')
ax3.set_title('Distance moyenne ')
ax3.set_xlabel('Taux de copieurs')
ax3.set_ylabel('Distance moyenne entre les voitures')
ax3.grid(True)
ax3.text(0.5, 1.05, f'Taille du monde: {taille_monde}, Pourcentage de voitures: {pourcentage_voitures}',
         horizontalalignment='center', transform=ax3.transAxes)

# Ajustement automatique de la disposition
plt.tight_layout()

# Affichage du plot
plt.show()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
