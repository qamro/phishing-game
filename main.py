import pygame
import random

pygame.init()

# set up the configuration and colors and fonts
WIDTH, HEIGHT = 800, 600
WATER_Y = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 32, True)

COLORS = {
    "orange": (255, 144, 40),
    "green": (90, 180, 70),
    "violet": (150, 80, 200)
}

score = 0
hook = {"x": 560, "y": 190, "state": "idle", "fish": None}
