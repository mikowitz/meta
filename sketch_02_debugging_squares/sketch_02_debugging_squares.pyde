import random
from Circle import Circle
from DebugSquare import DebugSquare

def setup():
    num_circles = 20
    size(800, 600)
    ellipseMode(RADIUS)
    fill(0, 0)
    stroke(0xFF00FFFF)
    smooth()
    global circles
    global debug_squares
    debug_squares = []
    circles = []
    for [i, j] in [[x, y] for x in range(0, width, 50) for y in range(0, height, 50)]:
        debug_squares.append(DebugSquare(i, j, 50))
        
    for i in range(0, num_circles):
        radius = random.randrange(20, 80)
        x = random.randrange(radius, width - radius)
        y = random.randrange(radius, height - radius)
        circles.append(Circle(x, y, radius))
        
def draw():
    background(0x000000)
    for d in debug_squares:
        d.draw()
    for c in circles:
        stroke(0xff00ffff)
        c.move()
        c.draw()
    



