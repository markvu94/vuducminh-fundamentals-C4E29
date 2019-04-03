from random import*
x = randint(1,100)

loop = True
while loop:
    n = int(input("guess my number = "))
    if n <x:
        print("too small")
    elif n > x:
        print("qua to")
      
    else:
        print("too big")
        loop = False


