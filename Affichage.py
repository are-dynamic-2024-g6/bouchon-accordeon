import pygame
import sys
import math


pygame.init()

# Définition de la taille de la fenêtre
WIDTH, HEIGHT = 800, 600
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

RADIUS = 200
ROAD_WIDTH = 50

CAR_RADIUS = 20  # Rayon des voitures

class Voiture:
    def __init__(self, position=None, conducteur=None, name=None, currentmove=0):
        self.position = position
        self.conducteur = conducteur
        self.name = name
        self.currentmove = currentmove

def draw_circle(screen, size):
    # Utilisation de la largeur et de la hauteur de l'écran
    center = (WIDTH // 2, HEIGHT // 2)
    
    # Calcul du rayon extérieur en fonction de la taille du monde
    max_cars = 100  # Nombre maximum de voitures que le monde peut accueillir
    min_radius = 50  # Rayon minimal du cercle extérieur
    max_radius = 500  # Rayon maximal du cercle extérieur (augmenté pour plus de voitures)
    outer_radius = min_radius + (max_radius - min_radius) * (size / max_cars)
    
    # Calcul de l'épaisseur du contour
    thickness = 30  # Épaisseur du contour du cercle
    
    # Dessiner le cercle gris extérieur
    pygame.draw.circle(screen, GRAY, center, int(outer_radius), thickness)
    
    # Dessiner le contour blanc intérieur
    inner_radius = outer_radius - 60  # Ajuster pour la taille des voitures
    pygame.draw.circle(screen, WHITE, center, int(inner_radius), 60)  # Augmenter l'épaisseur du contour blanc

def draw_cars_on_circle(screen, cars, zoom):
    num_cars = len(cars)
    angle_step = 2 * math.pi / num_cars
    
    
    
    for car in cars:
        # Calcul des coordonnées polaires de la position de la voiture
        angle = car.position * angle_step
        radius = RADIUS - ROAD_WIDTH / 2 - CAR_RADIUS  # Le rayon est ajusté pour placer la voiture à l'intérieur du cercle
        x = WIDTH // 2 + radius * math.cos(angle) * zoom * 3.7
        y = HEIGHT // 2 + radius * math.sin(angle) * zoom * 3.7
        
        # Dessiner la voiture
        pygame.draw.circle(screen, BLUE, (int(x), int(y)), int(CAR_RADIUS * zoom))

running = True
clock = pygame.time.Clock()
zoom = 1.0  # Facteur de zoom initial

# Exemple de création de voitures avec des positions aléatoires
cars = [Voiture(position=i) for i in range(20)]  # Liste de voitures avec des positions de 0 à 19

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Molette de la souris vers le haut (zoom in)
                zoom *= 1.1
            elif event.button == 5:  # Molette de la souris vers le bas (zoom out)
                zoom /= 1.1
    
    screen.fill(WHITE)
    draw_circle(screen, 100 * zoom)  # Appel de la fonction pour dessiner le cercle avec une épaisseur
    draw_cars_on_circle(screen, cars, zoom)  # Dessiner les voitures sur le cercle avec le zoom
    pygame.display.flip()

    clock.tick(60)

pygame.display.quit()
pygame.quit()
sys.exit()
