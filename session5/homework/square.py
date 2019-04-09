from turtle import *
def draw_square(l,c):
    """draw square with arguments of length (l) and border color (c)"""
    speed(0.5)
    color(c)
    for i in range(4):
        fd(l)
        left(90)

for i in range(30):
    draw_square(i*5,"red")
    left(17)
    penup()
    fd(i*2)
    pendown()