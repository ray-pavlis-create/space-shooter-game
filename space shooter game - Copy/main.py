import pygame
import random
from border import Border
from player import Player
from bullet import Bullet
from enemy import Enemy

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
bullet = Bullet(player.x, player.y, -5, 10, 10, WHITE)
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
    bullet.move()
    for enemy in enemies:
        enemy.move()
        
    # Draw
    window.fill(BLACK)
    border.draw(window)
    player.draw(window)
    bullet.draw(window)
    for enemy in enemies:
        enemy.draw(window)

    # Update Screen
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
