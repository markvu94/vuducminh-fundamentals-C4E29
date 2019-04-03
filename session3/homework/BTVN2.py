menu = ["red","blue","brown", "yellow","grey"]
from turtle import*
speed(0.5)
for i in range(len(menu)):
    for t in range (2):
        fillcolor(menu[i])
        begin_fill()

        fd(50)
        left(90)
        fd(100)
        left(90)

        end_fill()
    fd(50)
mainloop()