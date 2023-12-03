x=400


def setup():
    size(800,800)
def draw():
    global x
    strokeWeight(10)
    fill(245,183,116)
    ellipse(150,400,250,250)
    fill(255,0,0)
    triangle(36,350,150,100,264,350)
    strokeWeight(20)
    point(225,400)
    strokeWeight(5)
    fill(245,183,116)
    triangle(275,375,x,400,275,425)
    
    
    x=x+4
    
    
    
