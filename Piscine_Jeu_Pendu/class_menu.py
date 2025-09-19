import pygame
import subprocess
import os
from class_game import Game


class Menu:
    def __init__(self, screen, width, height, base_dir):
        self.screen = screen
        self.width = width
        self.height = height
        self.base_dir = base_dir
        self.clock = pygame.time.Clock()
        self.show_difficulty = False

        self.background = pygame.image.load(
            os.path.join(base_dir, "assets", "backGround.jpg")
        )
        self.background = pygame.transform.scale(self.background, (width, height))

        # Boutons
        self.button_color = (142, 255, 44)
        self.button_rect_close = pygame.Rect(width - 90, 20, 70, 30)
        self.button_rect_single = pygame.Rect(width // 2 - 150, 200, 300, 60)
        self.button_rect_multi = pygame.Rect(width // 2 - 150, 300, 300, 60)
        self.button_easy = pygame.Rect(width // 2 - 150, 200, 300, 60)
        self.button_medium = pygame.Rect(width // 2 - 150, 300, 300, 60)
        self.button_hard = pygame.Rect(width // 2 - 150, 400, 300, 60)

        # Textes
        self.font = pygame.font.Font(None, 40)
        self.text_button_close = pygame.font.Font(None, 25).render(
            "Close", True, (255, 255, 255)
        )
        self.text_button_single = self.font.render(
            "Single Player", True, (255, 255, 255)
        )
        self.text_button_multi = self.font.render("Multi Player", True, (255, 255, 255))
        self.text_button_easy = self.font.render("Easy (60s)", True, (255, 255, 255))
        self.text_button_medium = self.font.render(
            "Medium (30s)", True, (255, 255, 255)
        )
        self.text_button_hard = self.font.render("Hard (15s)", True, (255, 255, 255))
        self.title_font = pygame.font.Font(None, 60)

        self.single_player_path = os.path.join(base_dir, "single_player.py")
        self.multi_player_path = os.path.join(base_dir, "multi_player.py")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect_close.collidepoint(event.pos):
                        running = False
                    elif not self.show_difficulty:
                        if self.button_rect_single.collidepoint(event.pos):
                            self.show_difficulty = True
                        elif self.button_rect_multi.collidepoint(event.pos):
                            subprocess.run(["python", self.multi_player_path])
                    else:
                        if self.button_easy.collidepoint(event.pos):
                            self.start_game("Joueur 1", 60)
                            self.show_difficulty = False
                        elif self.button_medium.collidepoint(event.pos):
                            self.start_game("Joueur 1", 30)
                            self.show_difficulty = False
                        elif self.button_hard.collidepoint(event.pos):
                            self.start_game("Joueur 1", 15)
                            self.show_difficulty = False

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        title = self.title_font.render("Hangman Game", True, (200, 0, 0))
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))

        if not self.show_difficulty:
            self.draw_button(self.button_rect_single, self.text_button_single)
            self.draw_button(self.button_rect_multi, self.text_button_multi)
        else:
            self.draw_button(self.button_easy, self.text_button_easy)
            self.draw_button(self.button_medium, self.text_button_medium)
            self.draw_button(self.button_hard, self.text_button_hard)

        pygame.draw.rect(
            self.screen, self.button_color, self.button_rect_close, border_radius=10
        )
        self.screen.blit(
            self.text_button_close,
            (self.button_rect_close.x + 11, self.button_rect_close.y + 7),
        )

    def draw_button(self, rect, text_surface):
        pygame.draw.rect(self.screen, self.button_color, rect, border_radius=15)
        self.screen.blit(
            text_surface,
            (
                rect.centerx - text_surface.get_width() // 2,
                rect.centery - text_surface.get_height() // 2,
            ),
        )

    def start_game(self, player_name, temps_total):
        game = Game(
            self.screen,
            self.width,
            self.height,
            self.base_dir,
            player_name,
            temps_total,
        )
        game.run()
