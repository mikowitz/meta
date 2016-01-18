import random

def setup():
    num_circles = 20
    size(800, 600)
    ellipseMode(RADIUS)
    fill(0, 0)
    stroke(0xFF00FFFF)
    smooth()
    global circles
    circles = []
    for i in range(0, num_circles):
        radius = random.randrange(20, 80)
        x = random.randrange(radius, width - radius)
        y = random.randrange(radius, height - radius)
        circles.append(Circle(x, y, radius))
        
def draw():
    background(0x000000)
    for c in circles:
        c.move()
        stroke(0, 255, 255, 255)
        c.draw()
    
    
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
    
