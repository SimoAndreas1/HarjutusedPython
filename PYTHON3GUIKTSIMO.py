#KT Simo Andreas Novikov 2. kujund

import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(500,500)
aken.title("KT")

colors = ("red","blue", "green","orange")
turn = 0
spikes = 8
size = 10

kk = turtle.Turtle()

for i in range(spikes):
    kk.left(45)
    kk.forward(50)
    kk.left(90)
    kk.forward(50)
    
turtle.exitonclick()