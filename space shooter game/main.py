import pygame
from player import Player

# Pygame Setup
pygame.init()
bounds = (800, 600)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("!Space Fighters!")
clock = pygame.time.Clock()

# Global Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Program Variables
player = Player(400, 575, 25, 25, WHITE)

done = False

while not done:
    #Event Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Logic 
    player.move()
        
    # Draw
    window.fill(BLACK)
    player.draw(window)

    # Update Screen
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
