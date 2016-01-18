class DebugSquare(object):
    def __init__(self, x, y, dim):
        self.x = x
        self.y = y
        self.dim = dim
        self.upper_left = [x-dim, y-dim]
        self.upper_right = [x+dim, y-dim]
        self.lower_left = [x-dim, y+dim]
        self.lower_right = [x+dim, y+dim]
        
    def draw(self):
        rectMode(CORNERS)
        stroke(0xff005500)
        rect(*self.upper_left + self.lower_right)
                
        
