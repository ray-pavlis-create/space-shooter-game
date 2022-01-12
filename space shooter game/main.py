import pygame
from player import Player

pygame.init()
bounds = (300, 300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("!Space Fighters!")

block_size = 20
player = Player(block_size, bounds)