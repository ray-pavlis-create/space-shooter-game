import pygame

class Bullet:
    def __init__(self, initX, initY, deltaY, initW, initH, initColor):
        self.x = initX
        self.y = initY
        self.dy = deltaY
        self.w = initW
        self.h = initH
        self.color = initColor

    def move(self):
        self.y += self.dy

    def draw(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.w, self.h])