import pygame
import sys
import math
import time
import random

pygame.init()

# Définition de la taille de la fenêtre
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

font = pygame.font.SysFont(None, 30)

RADIUS = 200
ROAD_WIDTH = 50

CAR_RADIUS = 20  # Rayon des voitures
reaction_copieur = {
    (0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4, (0, 5): 5,
    (1, -1): 0, (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 4, (1, 4): 5,
    (2, -2): 0, (2, -1): 1, (2, 0): 2, (2, 1): 3, (2, 2): 4, (2, 3): 5,
    (3, -3): 0, (3, -2): 1, (3, -1): 2, (3, 0): 3, (3, 1): 4, (3, 2): 5,
    (4, -4): 0, (4, -3): 1, (4, -2): 2, (4, -1): 3, (4, 0): 4, (4, 1): 5,
    (5, -5): 0, (5, -4): 1, (5, -3): 2, (5, -2): 3, (5, -1): 4, (5, 0): 5
}

reaction_prudent = {
    (0, 0): [0], (0, 1): [1], (0, 2):[1,2] , (0, 3): [2,3], (0, 4): [3,4], (0, 5): [4,5],
    (1, -1): [0], (1, 0): [0,1], (1, 1): [1,2], (1, 2): [2,3], (1, 3): [3,4], (1, 4): [4,5],
    (2, -2): [0], (2, -1): [0,1], (2, 0): [1,2], (2, 1): [2,3], (2, 2): [3,4], (2, 3): [4,5],
    (3, -3): [0], (3, -2): [0,1], (3, -1): [1,2], (3, 0): [2,3], (3, 1): [3,4], (3, 2): [4,5],
    (4, -4): [0], (4, -3): [0,1], (4, -2): [1,2], (4, -1): [2,3], (4, 0): [3,4], (4, 1): [4,5],
    (5, -5): [0], (5, -4): [0,1], (5, -3): [1,2], (5, -2): [2,3], (5, -1): [3,4], (5, 0): [4,5]
}


class Voiture:
    def __init__(self, position=None, conducteur=None, name=None, currentmove=0):
        self.position = position
        self.conducteur = conducteur
        self.name = name
        self.currentmove = currentmove
        
def creer_monde(taille, pourcentage_voitures, pourcentage_de_copieur):
    monde = []
    classe_voiture = []
    nombres_voitures = int(taille * pourcentage_voitures) 
    espacement = taille // nombres_voitures
    cptnbcopieur=0
    
    for i in range(nombres_voitures):
        
        if cptnbcopieur/nombres_voitures < pourcentage_de_copieur:
            monde.append(Voiture(i*espacement,"C", "V" + str((nombres_voitures-1) - i)))
            classe_voiture.append("C")
            cptnbcopieur +=1
            
        else :
            monde.append(Voiture(i*espacement,"P","V" + str((nombres_voitures-1) - i)))
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
                elem.currentmove = random.choice(reaction_prudent[(elem.currentmove, temp_last - elem.currentmove)])
                elem.position = (elem.position + elem.currentmove) % taille
            
            
            temp_last = elem.currentmove
    
    return monde

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




# Calcul du rayon extérieur en fonction de la taille du monde
max_cars = 100  # Nombre maximum de voitures que le monde peut accueillir
min_radius = 50  # Rayon minimal du cercle extérieur
max_radius = 500  # Rayon maximal du cercle extérieur (augmenté pour plus de voitures)
ax_radius = 500  # Rayon maximal du cercle extérieur (augmenté pour plus de voitures)


def draw_circle(screen, size):
    # Utilisation de la largeur et de la hauteur de l'écran
    center = (WIDTH // 2, HEIGHT // 2)
    outer_radius = min_radius + (max_radius - min_radius) * (size / max_cars)
   
    
    # Calcul de l'épaisseur du contour
    thickness = 30  # Épaisseur du contour du cercle
    
    # Dessiner le cercle gris extérieur
    pygame.draw.circle(screen, GRAY, center, int(outer_radius), thickness)
    
    # Dessiner le contour blanc intérieur
    inner_radius = outer_radius - 60  # Ajuster pour la taille des voitures
    pygame.draw.circle(screen, WHITE, center, int(inner_radius), 60)  # Augmenter l'épaisseur du contour blanc

def draw_cars_on_circle(screen, cars, zoom,size):
    num_cars = len(cars)
    angle_step = 2 * math.pi / num_cars
    
    outer_radius = min_radius + (max_radius - min_radius) * (size / max_cars)
    
    for car in cars:
    
        # Calcul des coordonnées polaires de la position de la voiture
        angle = car.position * angle_step
         # Le rayon est ajusté pour placer la voiture à l'intérieur du cercle
        x = WIDTH // 2 + (outer_radius-15)  * math.cos(angle) *zoom 
        y = HEIGHT // 2 + (outer_radius-15) * math.sin(angle) *zoom
        # Dessiner la voiture
        if car.conducteur=='C':
            pygame.draw.circle(screen, BLUE, (int(x), int(y)), int(0.5*CAR_RADIUS))
        elif car.conducteur=='P':
            pygame.draw.circle(screen, RED, (int(x), int(y)), int(0.5*CAR_RADIUS))
        elif car.conducteur=='SPECIAL':
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), int(0.5*CAR_RADIUS))

running = True
clock = pygame.time.Clock()
zoom = 1.0  # Facteur de zoom initial
taille=50
pourcentage_voitures=0.6
pourcentage_de_copieur=0.5
monde_cree = creer_monde(taille, pourcentage_voitures, pourcentage_de_copieur)
cars = [Voiture(position=voiture.position, conducteur=voiture.conducteur, name=voiture.name) for voiture in monde_cree]
sequence = generer_sequence_vitesses(5)
# Exemple de création de voitures avec des positions aléatoires

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:# Molette de la souris vers le haut (zoom in)
                zoom *= 1.01
            elif event.button == 5:  # Molette de la souris vers le bas (zoom out)
                zoom /= 1.01
                
    screen.fill(WHITE)
    draw_circle(screen, taille * zoom )  # Appel de la fonction pour dessiner le cercle avec une épaisseur
    draw_cars_on_circle(screen, cars, zoom, taille)# Dessiner les voitures sur le cercle avec le zoom
    
    run_text1 = font.render("Tour : 1", True, BLACK)
    run_text2 = font.render("BLUE : Copieur", True, BLACK)
    run_text3 = font.render("RED : Prudent", True, BLACK)
    run_text4 = font.render("WHITE : Special", True, BLACK)
    run_text5 = font.render(f"Taille : {taille} ", True, BLACK)
    run_text6 = font.render(f"Pourcentage_voitures : {pourcentage_voitures} ", True, BLACK)
    run_text7 = font.render(f"Pourcentage_de_copieur : {pourcentage_de_copieur} ", True, BLACK)
    
    screen.blit(run_text1, (10, 10))
    screen.blit(run_text2, (10, 90))
    screen.blit(run_text3, (10, 110))
    screen.blit(run_text4, (10, 130))
    screen.blit(run_text5, (10, 30))
    screen.blit(run_text6, (10, 50))
    screen.blit(run_text7, (10, 70))
    time.sleep(5)
    pygame.display.flip()
    
    for vitesse in sequence:
        for i in range(2,6):
            monde_cree = deplacement(monde_cree, vitesse , taille)
            cars = [Voiture(position=voiture.position, conducteur=voiture.conducteur, name=voiture.name) for voiture in monde_cree]
            screen.fill(WHITE)
            draw_circle(screen, taille * zoom )  # Appel de la fonction pour dessiner le cercle avec une épaisseur
            draw_cars_on_circle(screen, cars, zoom, taille)# Dessiner les voitures sur le cercle avec le zoom
            run_text1 = font.render(f"Tour: {i}", True, BLACK)
            run_text2 = font.render("BLUE : Copieur", True, BLACK)
            run_text3 = font.render("RED : Prudent", True, BLACK)
            run_text4 = font.render("WHITE : Special", True, BLACK)
            run_text5 = font.render(f"Taille : {taille} ", True, BLACK)
            run_text6 = font.render(f"Pourcentage_voitures : {pourcentage_voitures} ", True, BLACK)
            run_text7 = font.render(f"Pourcentage_de_copieur : {pourcentage_de_copieur} ", True, BLACK)
        
            screen.blit(run_text1, (10, 10))
            screen.blit(run_text2, (10, 90))
            screen.blit(run_text3, (10, 110))
            screen.blit(run_text4, (10, 130))
            screen.blit(run_text5, (10, 30))
            screen.blit(run_text6, (10, 50))
            screen.blit(run_text7, (10, 70))
            time.sleep(5)
            pygame.display.flip()

clock.tick(60)


pygame.display.quit()
pygame.quit()
sys.exit()
