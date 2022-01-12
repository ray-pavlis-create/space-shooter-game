from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Player:
    direction = None
    body = None
    block_size = None
    color = (255, 255, 255)
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()

    def respawn(self):
        #self.body = ?
        self.direction = None

    def draw(self, game, window):
        game.draw.rect(window, self.color, self.block_size, self.block_size) #position???????