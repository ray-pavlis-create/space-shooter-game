import pygame

class Player:
    def __init__(self, initX, initY, initW, initH, initColor):
        self.x = initX
        self.y = initY
        self.w = initW
        self.h = initH
        self.color = initColor

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x += -5
            if self.x < 0:
                self.x = 0
        elif keys[pygame.K_RIGHT]:
            self.x += 5
            if self.x > 775:
                self.x = 775
        elif keys[pygame.K_UP]:
            self.y += -5
            if self.y < 380:
                self.y = 380
        elif keys[pygame.K_DOWN]:
            self.y += 5
            if self.y > 575:
                self.y = 575
            

    def draw(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.w, self.h])