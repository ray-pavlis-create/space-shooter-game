import pygame
from player import Player
from player import Direction

pygame.init()
bounds = (300, 300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("!Space Fighters!")

block_size = 20
player = Player(block_size, bounds)
done = False

while not done:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.steer(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            player.steer(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            player.steer(Direction.UP)
        elif keys[pygame.K_DOWN]:
            player.steer(Direction.DOWN)
        
    player.move()

    window.fill((0, 0, 0))
    player.draw(pygame, window)
    pygame.display.update()
