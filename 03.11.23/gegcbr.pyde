x=10



def setup():
    size(800,800)
    

def draw():
    global x
    x=x+5
    rotate(45)
    background(24,237,196)
    stroke(random(0,255))
    strokeWeight(random(0,100))
    point(x,10)
    
