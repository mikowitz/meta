import random

class Circle(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.dx = random.uniform(-1.0, 1.0)
        self.dy = random.uniform(-1.0, 1.0)
        
    def move(self):
        if self.x + self.r >= width or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r >= height or self.y - self.r <= 0:
            self.dy = -self.dy
            
        self.x += self.dx
        self.y += self.dy
        
    def draw(self):
        ellipse(self.x, self.y, self.r, self.r)

