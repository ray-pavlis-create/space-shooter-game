import pygame

class Enemy:
    def __init__(self, initX, initY, deltaX, deltaY, initW, initH, initColor):
        self.x = initX
        self.y = initY
        self.dx = deltaX
        self.dy = deltaY
        self.w = initW
        self.h = initH
        self.color = initColor

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
                self.dx *= -1
        elif self.x > 775:
                self.dx *= -1
        elif self.y < 0:
                self.dy *= -1
        elif self.y > 350:
                self.dy *= -1


    def draw(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.w, self.h])
