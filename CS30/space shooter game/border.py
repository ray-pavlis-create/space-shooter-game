import pygame

class Border:
    def __init__(self, initX, initY, initW, initH, initColor):
        self.x = initX
        self.y = initY
        self.w = initW
        self.h = initH
        self.color = initColor

    def draw(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.w, self.h])