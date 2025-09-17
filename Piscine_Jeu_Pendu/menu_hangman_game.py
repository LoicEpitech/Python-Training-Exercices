import os
import pygame
import sys
import subprocess

pygame.init()
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Hangman Game")
clock = pygame.time.Clock()

# backGr
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "assets", "backGround.jpg")
single_player_path = os.path.join(BASE_DIR, "single_player.py")
multi_player_path = os.path.join(BASE_DIR, "multi_player.py")
imageBackground = pygame.image.load(image_path)
imageBackground = pygame.transform.scale(imageBackground, (WIDTH, HEIGHT))

button_color = (142, 255, 44)
button_rect_close = pygame.Rect(WIDTH - 90, 20, 70, 30)

button_rect_single = pygame.Rect(WIDTH // 2 - 150, 200, 300, 60)
button_rect_multi = pygame.Rect(WIDTH // 2 - 150, 300, 300, 60)

font = pygame.font.Font(None, 40)
text_button_close = pygame.font.Font(None, 25).render("Close", True, (255, 255, 255))
text_button_single = font.render("Single Player", True, (255, 255, 255))
text_button_multi = font.render("Multi Player", True, (255, 255, 255))

# fonts
title_font = pygame.font.Font(None, 60)

# --- BOUCLE PRINCIPALE ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect_close.collidepoint(event.pos):
                running = False
            elif button_rect_single.collidepoint(event.pos):
                subprocess.run(["python", single_player_path])
            elif button_rect_multi.collidepoint(event.pos):
                subprocess.run(["python", multi_player_path])

    # BackInit
    screen.blit(imageBackground, (0, 0))

    # Titre
    title = title_font.render("Hangman Game", True, (200, 0, 0))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Bouton Single Player
    pygame.draw.rect(screen, button_color, button_rect_single, border_radius=15)
    screen.blit(
        text_button_single,
        (
            button_rect_single.centerx - text_button_single.get_width() // 2,
            button_rect_single.centery - text_button_single.get_height() // 2,
        ),
    )

    # Bouton Multi Player
    pygame.draw.rect(screen, button_color, button_rect_multi, border_radius=15)
    screen.blit(
        text_button_multi,
        (
            button_rect_multi.centerx - text_button_multi.get_width() // 2,
            button_rect_multi.centery - text_button_multi.get_height() // 2,
        ),
    )

    # Bouton fermer
    pygame.draw.rect(screen, button_color, button_rect_close, border_radius=10)
    screen.blit(text_button_close, (button_rect_close.x + 11, button_rect_close.y + 7))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
