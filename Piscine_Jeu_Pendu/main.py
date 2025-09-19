import pygame
import os
from class_menu import Menu

pygame.init()
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Hangman Game")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

menu = Menu(screen, WIDTH, HEIGHT, BASE_DIR)
menu.run()

pygame.quit()
