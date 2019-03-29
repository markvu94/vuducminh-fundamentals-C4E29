from turtle import *
speed (0.5)
color("black","yellow")

begin_fill()

for i in range(4):
    forward(100)
    left(90)

circle(-50,360,3)

end_fill()

pencolor("white")
left(180)
forward(200)

color("green","white")
begin_fill()

for i in range(36):
    circle(50,360)
    right(10)

end_fill()
mainloop ()