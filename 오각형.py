import  turtle, random
t=turtle.Turtle()
r=random.random()
g=random.random()
b=random.random()
t.color(r,g,b)
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(72)
t.end_fill()

