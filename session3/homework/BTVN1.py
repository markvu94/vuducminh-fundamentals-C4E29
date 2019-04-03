menu = ["red","blue","brown", "yellow","grey"]
from turtle import*
speed(0.5)
for i in range (len(menu)):
    for t in range (i+3):
        color(menu[i])
        fd(100)
        left(360/(i+3))
        
mainloop()