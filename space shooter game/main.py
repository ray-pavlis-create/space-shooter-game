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
bullets = []
enemies = []
for i in range(10):
    enemy = Enemy(random.randint(5, 750), random.randint(5, 350), random.randint(-5, 6), random.randint(-5, 6), 25, 25, RED)
    enemies.append(enemy)

# Collision detection
def rect_collide(rect1, rect2):
    le1 = rect1.x
    re1 = rect1.x + rect1.w
    te1 = rect1.y
    be1 = rect1.y + rect1.h

    le2 = rect2.x
    re2 = rect2.x + rect2.w
    te2 = rect2.y
    be2 = rect2.y + rect2.h

    if le1 < re2 and re1 > le2 and be1 > te2 and te1 < be2:
        return True
    else:
        return False

done = False

while not done:
    #Event Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.x, player.y, -5, 10, 10, WHITE)
                bullets.append(bullet)

    # Logic 
    player.move()
    for bullet in bullets:
        bullet.move()
    for enemy in enemies:
        enemy.move()

    for i in range(len(bullets)):
        for j in range(len(enemies) - 1, -1, -1):
            if rect_collide(bullets[i], enemies[j]):
                enemies.pop(j)
                enemy = Enemy(random.randint(5, 750), random.randint(5, 350), random.randint(-5, 6), random.randint(-5, 6), 25, 25, RED)
                enemies.append(enemy)
        
    # Draw
    window.fill(BLACK)
    border.draw(window)
    player.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    for enemy in enemies:
        enemy.draw(window)

    # Update Screen
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
