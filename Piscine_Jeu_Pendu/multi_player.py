import os
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Hangman Game - Multi")
clock = pygame.time.Clock()

# backGr
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "assets", "backGround.jpg")
imageBackground = pygame.image.load(image_path)
imageBackground = pygame.transform.scale(imageBackground, (WIDTH, HEIGHT))

button_color = (142, 255, 44)
button_rect = pygame.Rect(WIDTH - 90, 20, 70, 30)
font = pygame.font.Font(None, 25)
text_button = font.render("Close", True, (255, 255, 255))

# fonts
title_font = pygame.font.Font(None, 60)
word_font = pygame.font.Font(None, 50)
letters_font = pygame.font.Font(None, 30)

# variables
lettres_tapees = set()
lettres_trouvees = set()
nbEssai = 6
mot_cache = ""
theWord = ""
phase = "saisie"  # ⚡ phase = "saisie" puis "jeu"
mot_tape_par_j1 = ""


def dessiner_pendu(surface, erreurs):
    # la Base
    pygame.draw.line(surface, (0, 0, 0), (100, 515), (250, 515), 5)
    pygame.draw.line(surface, (0, 0, 0), (150, 515), (150, 225), 5)
    pygame.draw.line(surface, (0, 0, 0), (150, 300), (200, 225), 5)
    pygame.draw.line(surface, (0, 0, 0), (150, 225), (250, 225), 5)
    pygame.draw.line(surface, (0, 0, 0), (250, 225), (250, 250), 5)

    # Dessine les parties du corps selon erreurs
    if erreurs >= 1:
        pygame.draw.circle(surface, (0, 0, 0), (250, 270), 20, 3)
    if erreurs >= 2:
        pygame.draw.line(surface, (0, 0, 0), (250, 290), (250, 350), 3)
    if erreurs >= 3:
        pygame.draw.line(surface, (0, 0, 0), (250, 310), (230, 340), 3)
    if erreurs >= 4:
        pygame.draw.line(surface, (0, 0, 0), (250, 310), (270, 340), 3)
    if erreurs >= 5:
        pygame.draw.line(surface, (0, 0, 0), (250, 350), (230, 390), 3)
    if erreurs >= 6:
        pygame.draw.line(surface, (0, 0, 0), (250, 350), (270, 390), 3)


def proposer_lettre(lettre):
    global nbEssai, mot_cache
    lettre = lettre.lower()
    if lettre in lettres_tapees or not lettre.isalpha() or len(lettre) != 1:
        return
    lettres_tapees.add(lettre)

    if lettre in theWord:
        lettres_trouvees.add(lettre)
    else:
        nbEssai -= 1

    mot_cache = " ".join([l if l in lettres_trouvees else "_" for l in theWord])


# --- BOUCLE PRINCIPALE ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                running = False

        elif event.type == pygame.KEYDOWN:
            if phase == "saisie":
                if event.key == pygame.K_RETURN and len(mot_tape_par_j1) >= 4:
                    theWord = mot_tape_par_j1.lower()
                    mot_cache = "_ " * len(theWord)
                    phase = "jeu"
                elif event.key == pygame.K_BACKSPACE:
                    mot_tape_par_j1 = mot_tape_par_j1[:-1]
                elif event.unicode.isalpha():
                    mot_tape_par_j1 += event.unicode

            elif phase == "jeu":
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    proposer_lettre(event.unicode)

    # BackInit
    screen.blit(imageBackground, (0, 0))

    # Bouton fermer
    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    screen.blit(text_button, (button_rect.x + 11, button_rect.y + 7))

    if phase == "saisie":
        titre = title_font.render("Player 1: Type a word", True, (200, 0, 0))
        screen.blit(titre, (WIDTH // 2 - titre.get_width() // 2, 100))

        cache = "*" * len(mot_tape_par_j1)  # cacher les lettres tapées
        saisie_surface = word_font.render(cache, True, (0, 0, 0))
        screen.blit(saisie_surface, (WIDTH // 2 - saisie_surface.get_width() // 2, 200))

    else:  # phase == "jeu"
        # Titre
        title = title_font.render("Hangman Game", True, (200, 0, 0))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

        # Mot caché
        mot_surface = word_font.render(mot_cache, True, (0, 0, 0))
        screen.blit(mot_surface, (WIDTH // 2 - mot_surface.get_width() // 2, 150))

        lettres_proposees = ", ".join(sorted(lettres_tapees))

        # Lettres proposées
        ligneTitre = letters_font.render("Letters already proposed:", True, (0, 0, 0))
        ligneRep = letters_font.render(lettres_proposees, True, (0, 0, 0))

        screen.blit(ligneTitre, (350, 220))
        screen.blit(ligneRep, (350, 220 + ligneTitre.get_height() + 5))

        # Dessin du pendu
        dessiner_pendu(screen, 6 - nbEssai)

        # Vérifier victoire ou défaite
        if "_" not in mot_cache:
            win_text = title_font.render("You won !", True, (142, 255, 44))
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, 400))
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False
        elif nbEssai <= 0:
            lose_text = title_font.render(f"Lost ! Word : {theWord}", True, (255, 0, 0))
            screen.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, 400))
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
