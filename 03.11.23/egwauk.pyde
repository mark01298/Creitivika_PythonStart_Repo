x=50
y=50



def setup():
    size(100,100)
    strokeWeight(1)
   
def draw():
    global x
    global y
    global v
    global g
    x=x+5
    y=y-5
    background(24,256,196)
    fill(random(0,255))
    ellipse(x,x,10,10)
    ellipse(y,x,10,10)
    ellipse(y,y,10,10)
    ellipse(x,y,10,10)
    
    
