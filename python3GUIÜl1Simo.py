import turtle
import random

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Harjutus1")

colors = ('red','blue', 'orange', 'green')
turn = 0
spikes = 8
size = 10

for i in range (spikes):
    kk = turtle.Turtle()
    kk.color(random.choice(colors))
    kk.left(turn)
    kk.forward(100)
    turn+=45
    
turtle.exitonclick()