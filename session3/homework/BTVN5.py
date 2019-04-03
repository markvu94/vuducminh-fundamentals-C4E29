from random import *
x = "meticulous"
y = "champion"
z = "hexagon"
menu = [x,y,z]
shuffle (menu)
a = menu[0]
a1 = list(a)
shuffle (a1)
print (a1)
loop = True
while loop:
    answer = input("Your answer: ")
    if answer == a:
        print ("Hura")
        loop = False
    else:
        print(":(")


