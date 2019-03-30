from turtle import *
speed (0.5)

for i in range (3,7):
    if i %2 == 0:
        color("red")
    else:
        color("blue")
    for n in range (i):
        fd(100)
        left(360/i)

mainloop()



