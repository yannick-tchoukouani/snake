import pygame 
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
taille_case = 20
vitesse = 15

# Couleurs
couleur_fond = (0, 0, 0)
couleur_snake = (0, 255, 0)
couleur_pomme = (255, 0, 0)

# Direction initiale du serpent
direction = (1, 0)

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Snake Game")

# Fonction pour afficher le score
def afficher_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    fenetre.blit(text, (10, 10))

# Fonction principale du jeu
def jouer():
    global direction

    # Initialisation du serpent
    serpent = [(largeur_fenetre // 2, hauteur_fenetre // 2)]

    # Initialisation de la pomme
    pomme = nouvelle_pomme(serpent)

    # Initialisation du score
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Déplacement du serpent
        tete = (serpent[0][0] + direction[0] * taille_case, serpent[0][1] + direction[1] * taille_case)
        serpent.insert(0, tete)

        # Vérification des collisions avec la pomme
        if tete == pomme:
            score += 1
            pomme = nouvelle_pomme(serpent)
        else:
            serpent.pop()

        # Vérification des collisions avec soi-même
        if tete in serpent[1:]:
            fin_partie(score)

        # Vérification des collisions avec les bords
        if tete[0] < 0 or tete[0] >= largeur_fenetre or tete[1] < 0 or tete[1] >= hauteur_fenetre:
            fin_partie(score)

        # Affichage
        fenetre.fill(couleur_fond)
        for segment in serpent:
            pygame.draw.rect(fenetre, couleur_snake, (segment[0], segment[1], taille_case, taille_case))
        pygame.draw.rect(fenetre, couleur_pomme, (pomme[0], pomme[1], taille_case, taille_case))
        afficher_score(score)

        pygame.display.flip()
        pygame.time.Clock().tick(vitesse)

# Fonction pour générer une nouvelle pomme
def nouvelle_pomme(serpent):
    while True:
        pomme = (random.randint(0, (largeur_fenetre - taille_case) // taille_case) * taille_case,
                 random.randint(0, (hauteur_fenetre - taille_case) // taille_case) * taille_case)
        if pomme not in serpent:
            return pomme

# Fonction pour afficher l'écran de fin de partie
def fin_partie(score):
    font = pygame.font.Font(None, 72)
    text = font.render(f"Game Over - Score: {score}", True, (255, 255, 255))
    fenetre.blit(text, (largeur_fenetre // 4, hauteur_fenetre // 2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Lancer le jeu
jouer()
