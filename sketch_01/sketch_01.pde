int numCircles = 10;
Circle[] circles;

void setup() {
  size(800, 600);
  ellipseMode(RADIUS);
  fill(0, 0);
  stroke(0, 255, 255, 200);
  circles = new Circle[numCircles];
  for (int i = 0; i < numCircles; i++) {
    float r = random(50) + 20;
    circles[i] = new Circle(random(r, width - r), random(r, height - r), r);
  }
}

void draw() {
  background(0);
  for (int i = 0; i < numCircles; i++) {
    circles[i].move();
    circles[i].draw();
  }
}

class Circle {
  float x;
  float y;
  float r;
  float dx;
  float dy;
  
  Circle(float ix, float iy, float ir) {
    x = ix;
    y = iy;
    r = ir;
    dx = random(-1.0, 1.0);
    dy = random(-1.0, 1.0);
  }
  
  void move() {
    if (x + r >= width || x - r <= 0) {
      dx = -dx;
    }
    if (y + r >= height || y - r <= 0) {
      dy = -dy;
    }
    x += dx;
    y += dy;
  }
  
  void draw() {
    ellipse(x, y, r, r);
  }
}
    
