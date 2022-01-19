import pygame
import random
from player import Player
from enemy import Enemy
from border import Border

# Pygame Setup
pygame.init()
bounds = (800, 600)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("!Space Fighters!")
clock = pygame.time.Clock()

# Global Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (48, 48, 48)

# Program Variables
border = Border(0, 380, 800, 1, GRAY)
player = Player(400, 575, 25, 25, WHITE)
enemies = []
for i in range(10):
    enemy = Enemy(random.randint(5, 750), random.randint(5, 350), random.randint(-5, 6), random.randint(-5, 6), 25, 25, RED)
    enemies.append(enemy)

done = False

while not done:
    #Event Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Logic 
    player.move()
    for enemy in enemies:
        enemy.move()
        
    # Draw
    window.fill(BLACK)
    player.draw(window)
    for enemy in enemies:
        enemy.draw(window)
    border.draw(window)

    # Update Screen
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
